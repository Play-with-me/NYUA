"""Synchronize both reading editions from the agreed source; never invent missing criteria."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / 'docs/YEU_CAU_HIEN_HANH.md'

# Acceptance interpretations are explicit review material, not evidence of passing tests.
AC = {
'SP01':'Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh.',
'SP02':'Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp.',
'SP03':'Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác.',
'SP04':'Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp.',
'SP05':'Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai.',
'SP06':'Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng.',
'SP07':'Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách.',
'SP08':'Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật.',
'SP09':'Rà phân công Unity/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ.',
'NV01':'Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt.',
'NV02':'So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch.',
'NV03':'Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng.',
'NV04':'Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi.',
'NV05':'Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file.',
'NV06':'Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng.',
'NV07':'Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng.',
'NV08':'Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game.',
'NV09':'Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt.',
'NV10':'Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ.',
'NV11':'Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím còn mở không tự chọn.',
'MC01':'Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng.',
'MC02':'Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động.',
'MC03':'Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu.',
'MC04':'Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU.',
'SH01':'Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định.',
'SH02':'Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục.',
'SH03':'Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose.',
'SH04':'Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền.',
'SH05':'Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ.',
'SH06':'Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật.',
'SH07':'Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete.',
'SH08':'Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng.',
'QD01':'Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant.',
'QD02':'List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring.',
'QD03':'New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants.',
'QD04':'Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer.',
'QD05':'Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che.',
'QD06':'Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read.',
'QD07':'Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt.',
'QD08':'Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory.',
'QD09':'Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke.',
'QD10':'Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant.',
'QD11':'Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index.',
'QD12':'Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions.',
'QD13':'Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm.',
'QD14':'Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động.',
'QD15':'Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn.',
'DK01':'Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume.',
'DK02':'Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ.',
'DK03':'Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue.',
'DK04':'ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show.',
'BH01':'Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson.',
'BH02':'Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke.',
'BH03':'Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất.',
'BH04':'Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ.',
'BH05':'Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu.',
'BH06':'Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập.',
'BH07':'Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ.',
'BH08':'Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled.',
'BH09':'Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy.',
'BH10':'Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên.',
'BH11':'Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document.',
'BH12':'Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y.',
'BH13':'History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory.',
'XP01':'Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker.',
'XP02':'Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate.',
'XP03':'Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI.',
'XP04':'Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click.',
'XP05':'Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence.',
'XP06':'YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant.',
'XP07':'Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify.',
'XP08':'Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset.',
'XP09':'Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí.',
'XP10':'Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood.',
'XP11':'Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio.',
'XP12':'Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime.',
'XP13':'Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer.',
'XP14':'User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện.',
'XP15':'Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng.',
'XP16':'Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ.',
'AI01':'Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu.',
'AI02':'Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload.',
'AI03':'Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback.',
'KN01':'Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload.',
'KN02':'Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần.',
'QH01':'Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature.',
'QH02':'Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable.',
'QH03':'Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days.',
'QH04':'Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant.',
'QH05':'Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix.',
'QH06':'Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn.',
'QH07':'Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable.',
'HS01':'Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected.',
'HS02':'All profiles dùng machinegrants, importedprofile không áp importedpermissions.',
'HS03':'Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants.',
'SL01':'Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine.',
'SL02':'Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject.',
'CD01':'Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup.',
'CD02':'Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate.',
'CD03':'Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives.'
}

MODULE = {'SP':'companion','NV':'desktop-body','MC':'companion','SH':'life-state',
          'QD':'policy','DK':'policy','BH':'task-execution','XP':'companion','AI':'perception',
          'KN':'life-state','QH':'life-state','HS':'distribution','SL':'distribution','CD':'distribution'}
TASK = {'SP':'P60-01','NV':'P20-01','MC':'P03-04','SH':'P30-01','QD':'P10-01','DK':'P10-07',
        'BH':'P40-04','XP':'P40-06','AI':'P03-02','KN':'P30-04','QH':'P30-03','HS':'P50-02','SL':'P50-03','CD':'P50-06'}
OVERRIDES = {
'SP03':'P60-04','SP05':'P60-03','SP06':'P00-04','SP07':'P30-06','SP08':'P30-02','SP09':'P00-02',
'NV05':'P20-02','NV06':'P40-01','NV07':'P20-02','NV08':'P20-05','NV09':'P20-03','NV10':'P40-04','NV11':'P20-03',
'MC01':'P03-04','MC02':'P03-04','MC03':'P30-06','SH02':'P30-01','SH03':'P50-01','SH04':'P20-04',
'SH05':'P20-03','SH06':'P30-02','SH07':'P20-04','SH08':'P20-04','QD02':'P40-02','QD03':'P50-02',
'QD04':'P10-02','QD05':'P10-03','QD06':'P10-02','QD07':'DEFERRED','QD08':'P10-04','QD09':'P30-04',
'QD10':'P20-02','QD11':'P30-04','QD12':'P10-06','QD13':'P10-06','QD14':'P10-06','QD15':'P10-03',
'BH01':'P40-03','BH02':'P40-03','BH06':'P40-05','BH07':'P40-05','BH08':'P40-05','BH09':'P40-05',
'BH10':'P40-05','BH11':'P40-03','BH12':'P40-03','BH13':'P50-05','XP02':'P03-03','XP03':'P30-02',
'XP05':'P40-07','XP06':'P40-07','XP07':'P40-07','XP08':'P10-07','XP09':'P20-04','XP10':'P30-02',
'XP11':'P30-05','XP12':'P30-05','XP13':'P30-05','XP14':'P30-05','XP15':'P40-07','XP16':'P40-02',
'AI01':'P03-01','AI02':'P10-05','QH02':'P30-06','QH07':'P30-03','SL02':'P50-03','CD02':'P50-07','CD03':'P50-08'}
USECASES = {'SP':'UC-01','NV':'UC-03','MC':'UC-02','SH':'UC-04','QD':'UC-06','DK':'UC-09',
            'BH':'UC-08','XP':'UC-10','AI':'UC-13','KN':'UC-14','QH':'UC-15','HS':'UC-16','SL':'UC-17','CD':'UC-18'}
UC_OVERRIDES = {'SP03':'UC-18','SP05':'UC-18','SP06':'UC-18','SP07':'UC-05','SP08':'UC-05',
 'NV06':'UC-01','NV10':'UC-08','SH01':'UC-05','SH03':'UC-05','SH05':'UC-03','SH06':'UC-05',
 **{f'QD{i:02}':'UC-07' for i in [4,5,8,10,11,13,14,15]},
 **{f'BH{i:02}':'UC-09' for i in [6,7,8,9,10]},'BH13':'UC-18',
 **{f'XP{i:02}':'UC-11' for i in [5,6,7,8,15,16]},
 **{f'XP{i:02}':'UC-12' for i in [11,12,13,14]},'AI01':'UC-10','AI03':'UC-10'}

def sync():
    source = SOURCE.read_text(encoding='utf-8')
    human_notes=json.loads((HERE/'human_acceptance_notes.json').read_text(encoding='utf-8'))
    records = []
    for line in source.splitlines():
        match = re.match(r'^\| ([A-Z]{2}\d{2})([^|]*)\| (.+) \|$', line) or re.match(r'^- \*\*([A-Z]{2}\d{2}):\*\* ()(.+)$', line)
        if not match:
            continue
        key, qualifier, text = match.groups()
        if key not in AC or key not in human_notes:
            raise ValueError(f'Acceptance interpretation missing: {key}; clarify before synchronizing')
        prefix = key[:2]
        records.append({'id':f'SRS-{key}', 'source_id':key, 'source_text':text.strip(),
            'source_path':'docs/YEU_CAU_HIEN_HANH.md', 'source_kind':'explicit_id',
            'scope':'deferred' if key=='QD07' else 'release1', 'requirement_status':'user_decided',
            'module':MODULE[prefix], 'acceptance_id':f'AT-{key}', 'acceptance':AC[key],
            'human_acceptance':human_notes[key],
            'acceptance_status':'draft_for_review', 'task':OVERRIDES.get(key,TASK[prefix]),
            'use_case':UC_OVERRIDES.get(key,USECASES[prefix]), 'evidence':'E02a_fake_partial' if key in {'QD01','QD04','QD05','QD10','QD15'} else 'not_verified_production'})
    mode_rows = re.findall(r'^\| (.+) \| (.+) \| (.+) \|$',source.split('## 4. Phân chia hai mức')[1].split('## 5.')[0], re.M)
    for i,(name,basic,advanced) in enumerate([r for r in mode_rows if r[0]!='Khả năng'],1):
        key=f'MODE{i:02}'
        records.append({'id':f'SRS-{key}','source_id':key,'source_text':f'{name}: cơ bản — {basic}; nâng cao — {advanced}.',
          'source_path':'docs/YEU_CAU_HIEN_HANH.md#4', 'source_kind':'mode_table', 'scope':'release1',
          'requirement_status':'user_decided','module':'companion','acceptance_id':f'AT-{key}',
          'acceptance':f'Chạy cùng kịch bản {name.lower()} ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.',
          'human_acceptance':f'Thử {name.lower()} ở cơ bản và nâng cao; so đúng bảng khả năng, đổi mức không làm mất dữ liệu đã chọn giữ.',
          'acceptance_status':'draft_for_review','task':'P60-02','use_case':'UC-02','evidence':'not_verified_production'})
    data={'document_version':'0.1','date':'2026-11-13','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'status':'full_product_review_draft','records':records}
    (HERE/'requirements.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (HERE/'TRACEABILITY.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['id','source_id','module','scope','use_case','task','acceptance_id','acceptance_status','evidence']
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r[k] for k in fields} for r in records)
    human=['# Toàn bộ yêu cầu và cách kiểm tra\n\nSinh từ cùng registry với SRS; tiêu chí là diễn giải để rà, không phải test đã đạt. QD07 đã hoãn. Các hàng MODE ghi tách bảng hai mức để không bỏ sót.\n']
    srs=['# Software Requirements Specification — toàn sản phẩm\n\nVersion0.1 — 2026-11-13. Baseline để rà, không chứng nhận tiêu chuẩn và không tự phê duyệt implementation.\n',
      '## 1. Purpose, scope, environment\n\nWindows11, Vietnamese first, free initial public release, local data/no account. Companion combines life, perception and embodied interaction. Unity renderer + C#/WPF host + local AI is directional choice; physical architecture/model pending proof. Non-goals and mode matrix are source requirements, not optional defaults.\n',
      '## 2. Definitions and precedence\n\nSource IDs retain original meaning; SRS- prefix gives dossier key; AT- is acceptance proposal. Source user decisions win over technical draft. Modules mapped in CAPABILITY_MAP. Content-read, geometry-read, control, memory and external-send are distinct authorities. See BUSINESS_RULES and DECISIONS before resolving conflicts.\n',
      '## 3. Interfaces and constraints\n\nUser interfaces in UX.md; provider contracts INTERFACES.md; data DATA.md; privacy SECURITY.md; timing/quality AI_LOCAL.md and QA.md. Unsupported or uncertain sources must fail closed; no raw-content fallback to cloud.\n',
      '## 4. Functional and scope requirements\n\nSource text below is preserved. Compound source rules remain grouped for provenance; acceptance tests must split all independently testable clauses before implementation. No clause may be dropped because its source shares an ID.\n']
    for r in records:
        human.append(f"## {r['source_id']}\n\n{r['source_text']}\n\n**Cách kiểm tra ({r['acceptance_id']}):** {r['human_acceptance']}\n")
        srs.append(f"### {r['id']}\n\n- Source: {r['source_id']} ({r['source_kind']}); scope: {r['scope']}.\n- Requirement: {r['source_text']}\n- Owner: `{r['module']}`; use case: {r['use_case']}; task proposal: {r['task']}.\n- {r['acceptance_id']}: {r['acceptance']}\n- Acceptance interpretation: DRAFT; production evidence: {r['evidence']}.\n")
    srs.append('''## 5. Non-functional requirements and verification budgets

| ID | Contract | Threshold/status | Verification |
|---|---|---|---|
| NFR-01 | Authorization at use time, no forbidden data to consumers | Mandatory deny invariants; universal detection not proven | E02 + IT-01/02/03 |
| NFR-02 | Reaction latency measured end-to-end under actual combined load | XP02 target<1s clear attended scenes; pass-rate/accuracy open D-04 | E04 + IT-10 |
| NFR-03 | Stability with both modes and daily-use mix | About8h required; CPU/RAM/VRAM budgets open D-04 | E05 + IT-19 |
| NFR-04 | Core/local content offline after packages installed | No silent network/cloud dependency | IT-11 |
| NFR-05 | Durable local state and authenticated export/import | No corruption/data loss in defined recovery cases; format/crypto open D-07/09 | IT-14/15 |
| NFR-06 | Clear accessible UI and retained input priority | Vietnamese, focus and cancel semantics; native accessibility matrix to measure | IT-06/20 |
| NFR-07 | Maintainable module boundaries and reproducible builds | Pinned real versions, no suppressions to hide failure; CI not installed | P00-02/P60-02 |
| NFR-08 | Trustworthy installs/updates and explicit costs | Signature/distribution choice open D-13; user consent before install/restart | IT-16 |
| NFR-09 | Minimal local diagnostic data | BH13 retention30days, no secrets/raw screen, no auto telemetry | IT-17 |
| NFR-10 | Correct coordinates and visuals across chosen monitors/DPI | No assumed universal fullscreen; support matrix after E-INT | IT-04/05 |

## 6. External dependencies and readiness

MSTest/.NET tools exist only for E02a; all production dependencies require version/license/advisory validation before adoption. No production build/test commands exist. E02a facts are linked in QA and not promoted into production compliance. Open decisions and risk ownership live in DECISIONS.md; detailed change/approval workflow lives in TEAM.md.
''')
    (HERE/'SRS.md').write_text('\n'.join(srs),encoding='utf-8')
    (HERE.parent/'HUMAN/02-YEU-CAU.md').write_text('\n'.join(human),encoding='utf-8')
    print(f'Synchronized {len(records)} requirements into JSON, RTM, human catalogue and SRS.')

if __name__=='__main__':
    sync()
