"""Local diagram sources and PNG/SVG exports. No external rendering service."""
from pathlib import Path
import json
from xml.sax.saxutils import escape
from PIL import Image, ImageDraw, ImageFont

HERE=Path(__file__).resolve().parent
DIAGRAMS={
'01-context':('Phạm vi sản phẩm', '''flowchart LR
 User["Người dùng Windows 11"] --> App["Nhân vật đồng hành"]
 App --> Desktop["Desktop và app/website được phép"]
 App --> Local["Dữ liệu và AI trên máy"]
 App -.->|"Chữ được duyệt từng lần"| Cloud["AI ngoài tùy chọn"]
 App -.->|"Kiểm tra/tải, hỏi trước cài"| Update["Nguồn cập nhật tin cậy"]'''),
'02-containers':('Các phần chạy đề xuất', '''flowchart TB
 WPF["WPF settings / tray"] --> Host["C# host: policy, life, tasks, storage"]
 Godot["Godot renderer"] <-->|"Typed local messages: đề xuất"| Host
 Browser["Chrome / Edge bridge tùy chọn"] -->|"Evidence nguồn"| Host
 Windows["Windows adapter"] --> Host
 Host -->|"Safe snapshot"| AI["Local AI worker: đề xuất"]
 AI -->|"Validated observation"| Host
 Host --> Store[("Local state")]
 Host -.->|"Consented text only"| External["External AI"]'''),
'03-module-dependencies':('Phụ thuộc module, không phải luồng dữ liệu', '''flowchart LR
 policy --> desktopbody["desktop-body"]
 policy --> perception
 policy --> tasks["task-execution"]
 perception --> tasks
 desktopbody --> tasks
 life["life-state"] --> companion
 perception --> companion
 desktopbody --> companion
 tasks --> companion
 policy --> distribution
 life --> distribution'''),
'04-read-boundary':('Cổng quan sát an toàn', '''flowchart TD
 Source["Nguồn đang hiển thị"] --> Identity{"Identity / grants đủ?"}
 Identity -->|"Không"| Deny["Chặn, không phân tích"]
 Identity -->|"Có"| Private{"Riêng tư hoặc vùng nhạy cảm không chắc?"}
 Private -->|"Có"| Hold["Chặn cửa sổ; giữ hold nếu unsafe"]
 Private -->|"Không"| Filter["Lọc vùng cấm trước OCR/model"]
 Filter --> Rev{"Generation vẫn đúng?"}
 Rev -->|"Không"| Discard["Hủy dữ liệu/kết quả cũ"]
 Rev -->|"Có"| Safe["Safe snapshot tới local analysis"]
 Hold -->|"User bấm Thử đọc lại"| Identity
 Metadata["Chỉ geometry khi được phép"] --> Body["Sinh hoạt: không title/text"]'''),
'05-embodied-action':('Trình tự tới nút rồi bấm', '''sequenceDiagram
 participant User as Người dùng
 participant Host as Host và policy
 participant Body as Godot
 participant OS as Windows adapter
 User->>Host: Yêu cầu hoặc intent hợp lệ
 Host->>Host: Kiểm quyền, nguồn, input gate
 Host->>Body: Approach target + revisions
 Body-->>Host: Arrival report
 Host->>Host: Re-observe và final check
 alt Thay đổi hoặc user thao tác
 Host-->>Body: Dừng/yield, không bấm
 else Vẫn hợp lệ
 Host->>OS: Một input đã được phép
 OS-->>Host: Delivery result
 Host->>Host: Verify postcondition, không tự replay
 end'''),
'06-queue-state':('Trạng thái công việc và dừng', '''stateDiagram-v2
 [*] --> Queued
 Queued --> DelayedOnce: mood delay
 DelayedOnce --> Checking: xong hoạt động hoặc user yêu cầu lại
 Queued --> Checking: eligible
 Checking --> Approaching
 Approaching --> Rechecking
 Rechecking --> Acting: valid permit
 Acting --> Verifying
 Verifying --> Succeeded: postcondition true
 Checking --> FailedNeedsTeaching: mismatch
 Rechecking --> FailedNeedsTeaching: changed target
 Approaching --> YieldedHuman: human input
 YieldedHuman --> Checking: idle 60s and revalidate
 Queued --> Paused: stop/off/hide
 Paused --> Checking: explicit ResumeQueue and eligible
 Acting --> Cancelled: stop/off/hide
 Approaching --> Cancelled: stop/off/hide
 Queued --> Cancelled: exit/profile switch
 Paused --> Cancelled: exit/profile switch
 Succeeded --> [*]
 Cancelled --> [*]'''),
'07-life-relationship':('Quan hệ sâu: trạng thái đề xuất', '''stateDiagram-v2
 [*] --> Friends
 Friends --> Closer: positive interactions
 Closer --> Upset: repeated boundary violation or eligible neglect
 Upset --> Withdrawn: unresolved hurt
 Withdrawn --> SelfHidden: severity threshold TBD
 SelfHidden --> Reconnecting: invitation or gift accepted
 Reconnecting --> Closer: time and good treatment across sessions
 Upset --> Closer: gradual repair
 Closer --> RomanceExpression: user opt in and progression
 RomanceExpression --> Friends: user opt out respected
 note right of SelfHidden
 No content observation or control
 Settings and reset remain accessible
 end note'''),
'08-data-logical':('Mô hình dữ liệu logic, chưa physical schema', '''erDiagram
 INSTALLATION ||--o{ SOURCE_GRANT : owns
 INSTALLATION ||--o{ PROFILE : stores
 PROFILE ||--|| CHARACTER_STATE : has
 PROFILE ||--|| RELATIONSHIP_STATE : has
 PROFILE ||--o{ MEMORY : remembers
 MEMORY ||--o{ CONTRIBUTION : associates
 PROFILE ||--o{ LESSON : learns
 PROFILE ||--o{ PROP_STATE : contains
 PROFILE ||--o{ MEDIA_PREFERENCE : infers
 INSTALLATION ||--o{ ACTION_HISTORY : records
 PROFILE ||--o{ EXPORT_ARCHIVE : manually_exports
 INSTALLATION ||--o{ CREDENTIAL_REFERENCE : protects'''),
'09-backup':('Xuất/nhập và ranh giới dữ liệu', '''sequenceDiagram
 participant U as User
 participant H as Host
 participant F as Archive
 U->>H: Export chosen profile
 H->>U: Require password, explain recovery code
 U->>H: Password via secure UI
 H->>H: Whitelist data, exclude grants and keys
 H->>F: Authenticated encrypted data
 H-->>U: Recovery code held separately
 U->>H: Import file + password or recovery code
 H->>H: Validate format, limits, integrity and schema
 alt Valid
 H-->>U: New separate profile, current machine grants
 else Invalid
 H-->>U: Reject without altering existing profiles
 end'''),
'10-delivery':('Quy trình theo bằng chứng', '''flowchart TD
 Interview["User requirements"] --> Baseline["Two-edition dossier review"]
 Baseline --> Probes["E02a / Godot E-INT / local AI probes"]
 Probes --> Decision{"Evidence enough?"}
 Decision -->|"No"| Review["Report limits and user tradeoff"]
 Review --> Baseline
 Decision -->|"Yes"| Spec["Approve scoped spec and task plan"]
 Spec --> Build["Small implementation slice"]
 Build --> Verify["Tests, review, real runtime"]
 Verify --> User["User acceptance"]
 User --> Integration["Both modes / offline / 8h / data / release checks"]
 Integration --> Release["User approves public artifact"]'''),
'11-media':('Tự mở nội dung ở nâng cao', '''flowchart TD
 Start["Advanced own-media intent"] --> Gate{"Idle enough, unlocked, no media?"}
 Gate -->|"No"| Life["Self life; no interruption"]
 Gate -->|"Yes"| Grants{"Chosen browser and site allowed?"}
 Grants -->|"No"| Life
 Grants -->|"Yes"| Tab["Own tab; preserve user tabs"]
 Tab --> Free{"Free and accessible?"}
 Free -->|"Yes"| Play["Play; yield controls on user return"]
 Free -->|"No"| Count{"Fewer than 3 candidates?"}
 Count -->|"Yes"| Tab
 Count -->|"No"| Life'''),
'12-ui-map':('Bản đồ màn hình đề xuất', '''flowchart LR
 First["First run: name / startup / mode"] --> Living["Desktop avatar"]
 Tray["Tray click"] --> Settings["Full settings"]
 Living --> Context["Right click: Food / Cleanup"]
 Settings --> Character["Character / size / monitors"]
 Settings --> Mode["Modes / packages / hardware"]
 Settings --> Permission["App / site / frame permissions"]
 Settings --> Tasks["Lessons / queue"]
 Settings --> Memory["Memories / relationship"]
 Settings --> Profiles["Profiles / export / import"]
 Settings --> History["Local history / startup / updates / help"]'''),
'13-profile-clock':('Đóng app khác chuyển hồ sơ', '''stateDiagram-v2
 [*] --> Active
 Active --> AppClosed: controlled exit, queue cancelled
 AppClosed --> Active: elapsed reconcile, no fabricated events
 Active --> InactiveFrozen: switch profile, queue cancelled
 InactiveFrozen --> Active: resume exact frozen state
 Active --> Resetting: explicit reset current
 Resetting --> Active: initial state, lessons cleared
 note right of InactiveFrozen
 No hunger, mood, relation or clock progress
 Shared installation grants unchanged
 end note'''),
'14-ai-timing':('Đo phản ứng toàn luồng', '''flowchart LR
 T0["Scene visible t0"] --> T1["Eligibility and filtering t1"]
 T1 --> T2["Safe snapshot and OCR t2"]
 T2 --> T3["Local inference t3"]
 T3 --> T4["Validate and mood decision t4"]
 T4 --> T5["Animation starts t5"]
 T5 --> Measure["Measure t5 minus t0, quality and load"]''')
}

def write_mermaid():
    tasks=json.loads((HERE.parent/'AI/backlog.json').read_text(encoding='utf-8'))['tasks']
    task_graph=['flowchart TD']
    for phase in dict.fromkeys(t['id'].split('-')[0] for t in tasks):
        task_graph.append(f' subgraph {phase}["{phase}"]')
        for t in tasks:
            if t['id'].startswith(phase+'-'):
                task_graph.append(f'  {t["id"].replace("-","_")}["{t["id"]}: {t["title"]}"]')
        task_graph.append(' end')
    for t in tasks:
        for dep in t['dependencies']:task_graph.append(f' {dep.replace("-","_")} --> {t["id"].replace("-","_")}')
    DIAGRAMS['15-task-dependencies']=('Toàn bộ phụ thuộc task từ backlog, chưa ủy quyền thực thi','\n'.join(task_graph))
    atlas=['# Atlas sơ đồ — bản vẽ chi tiết\n\nMọi topology/state design chưa được duyệt được hiểu là đề xuất. Sơ đồ không phải Graphify code extraction. Bản PNG/SVG tổng quan dễ đọc đi kèm.\n']
    index=['# Sơ đồ và bản vẽ\n\nPNG để xem trực tiếp; SVG để phóng/in; Mermaid .mmd là nguồn sửa được. Không gửi sơ đồ tới dịch vụ render bên ngoài.\n',
      '- [Kiến trúc PNG](architecture.png) / [SVG](architecture.svg)\n- [Quy trình PNG](delivery.png) / [SVG](delivery.svg)\n- [Cổng quyền PNG](permissions.png) / [SVG](permissions.svg)\n- [Dữ liệu PNG](data.png) / [SVG](data.svg)\n- [Atlas có 15 sơ đồ Mermaid](ATLAS.md)\n']
    for name,(title,code) in DIAGRAMS.items():
        (HERE/f'{name}.mmd').write_text(code+'\n',encoding='utf-8')
        atlas.append(f'## {name} — {title}\n\n```mermaid\n{code}\n```\n')
        index.append(f'- [{name}: {title}]({name}.mmd)\n')
    (HERE/'ATLAS.md').write_text('\n'.join(atlas),encoding='utf-8')
    (HERE/'README.md').write_text('\n'.join(index),encoding='utf-8')

def drawing(name,title,subtitle,nodes,edges,size=(1800,1240)):
    img=Image.new('RGB',size,'#f5f6f8'); d=ImageDraw.Draw(img)
    fontpath=Path('C:/Windows/Fonts/segoeui.ttf')
    boldpath=Path('C:/Windows/Fonts/seguisb.ttf')
    font=ImageFont.truetype(str(fontpath),24)
    head=ImageFont.truetype(str(boldpath),30)
    titlefont=ImageFont.truetype(str(boldpath),42)
    small=ImageFont.truetype(str(fontpath),22)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{size[0]}" height="{size[1]}" viewBox="0 0 {size[0]} {size[1]}">',
         '<rect width="100%" height="100%" fill="#f5f6f8"/>',
         '<defs><marker id="a" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10" fill="#5c726d"/></marker></defs>']
    def text(x,y,s,f,px,fill='#202b38'):
        d.text((x,y),s,font=f,fill=fill)
        svg.append(f'<text x="{x}" y="{y+px}" fill="{fill}" font-family="Segoe UI, sans-serif" font-size="{px}">{escape(s)}</text>')
    text(64,35,title,titlefont,42);text(64,100,subtitle,small,22)
    for a,b,label in edges:
        ax,ay,aw,ah,*_=nodes[a]; bx,by,bw,bh,*_=nodes[b]
        if ax==bx:
            start=(ax+aw/2,ay+ah) if by>ay else (ax+aw/2,ay)
            end=(bx+bw/2,by) if by>ay else (bx+bw/2,by+bh)
            pts=[start,end]
        else:
            start=(ax+aw,ay+ah/2) if bx>ax else (ax,ay+ah/2)
            end=(bx,by+bh/2) if bx>ax else (bx+bw,by+bh/2)
            mid=(start[0]+end[0])/2
            pts=[start,(mid,start[1]),(mid,end[1]),end]
        d.line(pts,fill='#5c726d',width=4)
        ex,ey=end; prev=pts[-2];dx=ex-prev[0];dy=ey-prev[1]
        if abs(dx)>abs(dy): arrow=[end,(ex-(12 if dx>0 else -12),ey-7),(ex-(12 if dx>0 else -12),ey+7)]
        else: arrow=[end,(ex-7,ey-(12 if dy>0 else -12)),(ex+7,ey-(12 if dy>0 else -12))]
        d.polygon(arrow,fill='#5c726d')
        svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="none" stroke="#5c726d" stroke-width="4" marker-end="url(#a)"/>')
        if label:
            lx=(start[0]+end[0])/2;ly=(start[1]+end[1])/2-32
            box=d.textbbox((0,0),label,font=small);tw=box[2]
            d.rectangle((lx-tw/2-8,ly,lx+tw/2+8,ly+30),fill='#f5f6f8')
            text(lx-tw/2,ly,label,small,22)
    for x,y,w,h,label,detail in nodes.values():
        d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill='white',outline='#b8cdc6',width=2)
        d.rectangle((x,y+12,x+5,y+h-12),fill='#155e52')
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#b8cdc6" stroke-width="2"/>')
        text(x+22,y+14,label,head,30)
        cy=y+58
        for paragraph in detail.split('\n'):
            line=''
            for word in paragraph.split():
                candidate=(line+' '+word).strip()
                if d.textlength(candidate,font=font)>w-44 and line:
                    text(x+22,cy,line,font,24);cy+=32;line=word
                else:line=candidate
            if line:text(x+22,cy,line,font,24);cy+=32
        if cy>y+h: raise ValueError(f'Text overflow: {name}/{label}')
    text(64,size[1]-52,'2026-11-13 · Bản thiết kế để rà; các phần chưa thử không được coi là đã hoạt động.',small,22)
    svg.append('</svg>')
    img.save(HERE/f'{name}.png');(HERE/f'{name}.svg').write_text('\n'.join(svg),encoding='utf-8')

def main():
    write_mermaid()
    drawing('architecture','Bản đồ hệ thống: ai làm việc gì?','Hướng đã chọn: Godot + C#/WPF + AI local. Cách kết nối cụ thể vẫn cần phép thử.',{
      'user':(60,200,440,150,'Người dùng','Quyết định trải nghiệm, quyền, chi phí và nghiệm thu.'),
      'wpf':(680,200,440,150,'WPF: ứng dụng quản lý','Cài đặt, hồ sơ, bài học, hàng đợi, ký ức, dừng/ẩn.'),
      'unity':(1300,200,440,180,'Godot: nhân vật','Hoạt ảnh, biểu cảm, di chuyển và đồ vật. Không tự cấp quyền.'),
      'source':(60,570,440,180,'Windows / Chrome / Edge','Nguồn và hình học được phép. Không mặc định mọi app đều hỗ trợ.'),
      'host':(680,530,440,240,'C# Host: điều phối','Policy kiểm quyền tại lúc dùng.\nĐời sống, ký ức và tác vụ.\nLọc nội dung trước phân tích.'),
      'ai':(1300,570,440,180,'AI local','Hiểu ngữ cảnh an toàn, trả nhận định. Không phát click hoặc mở quyền.'),
      'data':(680,960,440,150,'Dữ liệu trên máy','Trạng thái bình thường; chỉ backup khi bạn bấm xuất.'),
      'outside':(1300,960,440,150,'AI ngoài: tùy chọn','Chỉ chữ bạn chủ động xem và duyệt cho từng lần gửi.')},
      [('user','wpf',''),('wpf','host','Lệnh người dùng'),('source','host',''),('host','unity','Hoạt ảnh'),('host','ai','Dữ liệu an toàn'),('host','data','Lưu cục bộ'),('host','outside','Duyệt từng lần')])
    delivery={}
    labels=[('Rà yêu cầu và SRS','Hai bản cùng nguồn; chỗ chưa biết ghi rõ.'),('Thử các rủi ro chính','Quyền nguồn, Godot desktop, AI local.'),('Duyệt lát làm tiếp','Spec + hợp đồng + task + tiêu chí kiểm.'),('Xây và kiểm tra nhỏ','Code, test, rà soát và chạy thật.'),('Người dùng dùng thử','Chưa dùng thử không ghi nghiệm thu.'),('Tích hợp và phát hành','Hai mức, offline, 8 giờ, dữ liệu, giấy phép.')]
    for i,(a,b) in enumerate(labels):delivery[str(i)]=(340,180+i*190,1120,130,a,b)
    drawing('delivery','Quy trình phát triển theo bằng chứng','Không qua bước chỉ vì đã viết tài liệu; không tự hạ yêu cầu để báo đạt.',delivery,[(str(i),str(i+1),'') for i in range(5)],(1800,1450))
    drawing('permissions','Cổng quyền trước khi phân tích','Sơ đồ ý nghĩa; nhận dạng vùng thật chưa được chứng minh bởi mẫu E02a.',{
      'source':(80,200,500,160,'Nguồn đang hiển thị','Danh tính app / website / khung cần xác định.'),
      'grant':(80,500,500,160,'Kiểm quyền và trạng thái','Đủ cả trình duyệt và website, không riêng tư, không tắt/ẩn.'),
      'safe':(80,800,500,180,'Lọc và kiểm an toàn','Không chắc thì chặn cửa sổ. Kiểm lại phiên bản quyền và nguồn trước giao.'),
      'analysis':(80,1120,500,160,'Chỉ nội dung an toàn','OCR / AI / quyết định / ký ức tuân theo nguồn và mục đích.'),
      'deny':(1000,500,650,160,'Chặn hoặc hủy','Không có nội dung tới phần phân tích; giải thích lý do.'),
      'retry':(1000,820,650,180,'Thử đọc lại','Bạn bấm mới kiểm tra lại. Nút không bỏ qua bộ lọc.'),
      'geometry':(1000,1120,650,160,'Ngoại lệ chỉ hình học','Vị trí/kích thước để sinh hoạt; không tiêu đề/nội dung.')},
      [('source','grant',''),('grant','safe','Hợp lệ'),('safe','analysis','Vẫn an toàn'),('grant','deny','Không hợp lệ'),('safe','retry','Chưa chắc')],(1800,1450))
    drawing('data','Bản đồ dữ liệu theo phạm vi','Mô hình logic đề xuất; chưa chốt cơ sở dữ liệu hoặc thuật toán mã hóa.',{
      'installation':(80,200,500,160,'Theo máy / ứng dụng','Quyền chung, startup, chọn trình duyệt và màn hình.'),
      'profile':(690,200,1030,160,'Theo từng hồ sơ','Một hồ sơ hoạt động. Hồ sơ khác đóng băng hoàn toàn.'),
      'state':(690,540,440,170,'Đời sống / quan hệ','Nhu cầu, tâm trạng, tính cách, ký ức và sở thích.'),
      'lesson':(1300,540,420,170,'Bài học / đồ vật','Reset hồ sơ xóa bài học; queue chưa xong không tự chạy lại.'),
      'history':(80,900,500,170,'Lịch sử thao tác','Riêng với ký ức; giữ 30 ngày, không ảnh/chữ riêng tư.'),
      'archive':(690,900,440,170,'Bản xuất thủ công','Mật khẩu và mã khôi phục. Không quyền hiệu lực hoặc khóa AI.'),
      'key':(1300,900,420,170,'Khóa AI trên máy','Không đưa vào bản sao lưu. Máy mới phải kết nối lại.')},
      [('installation','profile',''),('profile','state',''),('profile','lesson',''),('state','archive','Xuất theo lựa chọn')])
    print(f'Generated {len(DIAGRAMS)} Mermaid sources, atlas, and 4 PNG/SVG diagrams locally.')

if __name__=='__main__':main()
