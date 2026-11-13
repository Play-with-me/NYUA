# Atlas sơ đồ — bản vẽ chi tiết

Mọi topology/state design chưa được duyệt được hiểu là đề xuất. Sơ đồ không phải Graphify code extraction. Bản PNG/SVG tổng quan dễ đọc đi kèm.

## 01-context — Phạm vi sản phẩm

```mermaid
flowchart LR
 User["Người dùng Windows 11"] --> App["Nhân vật đồng hành"]
 App --> Desktop["Desktop và app/website được phép"]
 App --> Local["Dữ liệu và AI trên máy"]
 App -.->|"Chữ được duyệt từng lần"| Cloud["AI ngoài tùy chọn"]
 App -.->|"Kiểm tra/tải, hỏi trước cài"| Update["Nguồn cập nhật tin cậy"]
```

## 02-containers — Các phần chạy đề xuất

```mermaid
flowchart TB
 WPF["WPF settings / tray"] --> Host["C# host: policy, life, tasks, storage"]
 Unity["Unity renderer"] <-->|"Typed local messages: đề xuất"| Host
 Browser["Chrome / Edge bridge tùy chọn"] -->|"Evidence nguồn"| Host
 Windows["Windows adapter"] --> Host
 Host -->|"Safe snapshot"| AI["Local AI worker: đề xuất"]
 AI -->|"Validated observation"| Host
 Host --> Store[("Local state")]
 Host -.->|"Consented text only"| External["External AI"]
```

## 03-module-dependencies — Phụ thuộc module, không phải luồng dữ liệu

```mermaid
flowchart LR
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
 life --> distribution
```

## 04-read-boundary — Cổng quan sát an toàn

```mermaid
flowchart TD
 Source["Nguồn đang hiển thị"] --> Identity{"Identity / grants đủ?"}
 Identity -->|"Không"| Deny["Chặn, không phân tích"]
 Identity -->|"Có"| Private{"Riêng tư hoặc vùng nhạy cảm không chắc?"}
 Private -->|"Có"| Hold["Chặn cửa sổ; giữ hold nếu unsafe"]
 Private -->|"Không"| Filter["Lọc vùng cấm trước OCR/model"]
 Filter --> Rev{"Generation vẫn đúng?"}
 Rev -->|"Không"| Discard["Hủy dữ liệu/kết quả cũ"]
 Rev -->|"Có"| Safe["Safe snapshot tới local analysis"]
 Hold -->|"User bấm Thử đọc lại"| Identity
 Metadata["Chỉ geometry khi được phép"] --> Body["Sinh hoạt: không title/text"]
```

## 05-embodied-action — Trình tự tới nút rồi bấm

```mermaid
sequenceDiagram
 participant User as Người dùng
 participant Host as Host và policy
 participant Body as Unity
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
 end
```

## 06-queue-state — Trạng thái công việc và dừng

```mermaid
stateDiagram-v2
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
 Cancelled --> [*]
```

## 07-life-relationship — Quan hệ sâu: trạng thái đề xuất

```mermaid
stateDiagram-v2
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
 end note
```

## 08-data-logical — Mô hình dữ liệu logic, chưa physical schema

```mermaid
erDiagram
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
 INSTALLATION ||--o{ CREDENTIAL_REFERENCE : protects
```

## 09-backup — Xuất/nhập và ranh giới dữ liệu

```mermaid
sequenceDiagram
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
 end
```

## 10-delivery — Quy trình theo bằng chứng

```mermaid
flowchart TD
 Interview["User requirements"] --> Baseline["Two-edition dossier review"]
 Baseline --> Probes["E02a / Unity E-INT / local AI probes"]
 Probes --> Decision{"Evidence enough?"}
 Decision -->|"No"| Review["Report limits and user tradeoff"]
 Review --> Baseline
 Decision -->|"Yes"| Spec["Approve scoped spec and task plan"]
 Spec --> Build["Small implementation slice"]
 Build --> Verify["Tests, review, real runtime"]
 Verify --> User["User acceptance"]
 User --> Integration["Both modes / offline / 8h / data / release checks"]
 Integration --> Release["User approves public artifact"]
```

## 11-media — Tự mở nội dung ở nâng cao

```mermaid
flowchart TD
 Start["Advanced own-media intent"] --> Gate{"Idle enough, unlocked, no media?"}
 Gate -->|"No"| Life["Self life; no interruption"]
 Gate -->|"Yes"| Grants{"Chosen browser and site allowed?"}
 Grants -->|"No"| Life
 Grants -->|"Yes"| Tab["Own tab; preserve user tabs"]
 Tab --> Free{"Free and accessible?"}
 Free -->|"Yes"| Play["Play; yield controls on user return"]
 Free -->|"No"| Count{"Fewer than 3 candidates?"}
 Count -->|"Yes"| Tab
 Count -->|"No"| Life
```

## 12-ui-map — Bản đồ màn hình đề xuất

```mermaid
flowchart LR
 First["First run: name / startup / mode"] --> Living["Desktop avatar"]
 Tray["Tray click"] --> Settings["Full settings"]
 Living --> Context["Right click: Food / Cleanup"]
 Settings --> Character["Character / size / monitors"]
 Settings --> Mode["Modes / packages / hardware"]
 Settings --> Permission["App / site / frame permissions"]
 Settings --> Tasks["Lessons / queue"]
 Settings --> Memory["Memories / relationship"]
 Settings --> Profiles["Profiles / export / import"]
 Settings --> History["Local history / startup / updates / help"]
```

## 13-profile-clock — Đóng app khác chuyển hồ sơ

```mermaid
stateDiagram-v2
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
 end note
```

## 14-ai-timing — Đo phản ứng toàn luồng

```mermaid
flowchart LR
 T0["Scene visible t0"] --> T1["Eligibility and filtering t1"]
 T1 --> T2["Safe snapshot and OCR t2"]
 T2 --> T3["Local inference t3"]
 T3 --> T4["Validate and mood decision t4"]
 T4 --> T5["Animation starts t5"]
 T5 --> Measure["Measure t5 minus t0, quality and load"]
```

## 15-task-dependencies — Toàn bộ phụ thuộc task từ backlog, chưa ủy quyền thực thi

```mermaid
flowchart TD
 subgraph P00["P00"]
  P00_01["P00-01: Rà baseline và giải quyết mâu thuẫn phạm vi"]
  P00_02["P00-02: Rà ranh giới và hợp đồng hybrid"]
  P00_03["P00-03: Chốt tiêu chuẩn chất lượng sau đo"]
  P00_04["P00-04: Lập danh mục giấy phép và chi phí"]
 end
 subgraph P01["P01"]
  P01_01["P01-01: Khép kiểm tra UI còn mở của E02a"]
 end
 subgraph P02["P02"]
  P02_01["P02-01: Chọn và dựng renderer thử tối thiểu"]
  P02_02["P02-02: Thử transparent overlay và hit regions"]
  P02_03["P02-03: Thử tọa độ qua monitor và DPI"]
  P02_04["P02-04: Thử kết nối typed host-renderer"]
  P02_05["P02-05: Thử mất kết nối và khôi phục an toàn"]
 end
 subgraph P03["P03"]
  P03_01["P03-01: Sàng lọc model/runtime local có quyền phân phối"]
  P03_02["P03-02: Dựng benchmark dữ liệu cảnh an toàn"]
  P03_03["P03-03: Đo phản ứng toàn luồng dưới tải kết hợp"]
  P03_04["P03-04: Đề xuất hai mức và luồng gói nâng cao"]
 end
 subgraph P10["P10"]
  P10_01["P10-01: Triển khai grants mặc định tắt và read/control"]
  P10_02["P10-02: Nhận dạng nguồn và vùng đang hiển thị"]
  P10_03["P10-03: Lọc sensitive/private và retry hold trên nguồn thật"]
  P10_04["P10-04: Kiểm chứng clipboard history đúng Win+V scope"]
  P10_05["P10-05: Luồng AI ngoài có preview và consent mỗi lần"]
  P10_06["P10-06: Bridge trình duyệt và ngoại lệ khung video"]
  P10_07["P10-07: Input arbitration và các nút dừng"]
 end
 subgraph P20["P20"]
  P20_01["P20-01: Duyệt model sheet nhân vật gốc"]
  P20_02["P20-02: Di chuyển và bề mặt cửa sổ"]
  P20_03["P20-03: Pet/lift/throw và chuyển vị trí an toàn"]
  P20_04["P20-04: Foodtray, đồ vật và animatedcleanup"]
  P20_05["P20-05: Placement nhiều màn hình và fullscreen"]
 end
 subgraph P30["P30"]
  P30_01["P30-01: Needs/sleep/rest và elapsed reconciliation"]
  P30_02["P30-02: Lựa chọn hoạt động, mood và attention limits"]
  P30_03["P30-03: Quan hệ sâu, neglect và làm lành"]
  P30_04["P30-04: Memory provenance, pin/fade/edit/delete"]
  P30_05["P30-05: Học gu từ user media evidence"]
  P30_06["P30-06: Mode preservation, personality và romance opt-in"]
 end
 subgraph P40["P40"]
  P40_01["P40-01: Onboarding/tray/settings shell"]
  P40_02["P40-02: UI grants và chosenbrowser"]
  P40_03["P40-03: Dạy/review/manage lesson và searchparameters"]
  P40_04["P40-04: Embodied execution và postconditionverify"]
  P40_05["P40-05: Hàng đợi, priority và stop lifecycle"]
  P40_06["P40-06: Xem cùng và phản ứng cảm xúc"]
  P40_07["P40-07: Tự tìm/mở nội dung trong quyền"]
 end
 subgraph P50["P50"]
  P50_01["P50-01: Chốt storage và transaction/persistence"]
  P50_02["P50-02: Profile import/switch/reset semantics"]
  P50_03["P50-03: Manualexport password/recovery format"]
  P50_04["P50-04: Validate/import archive thành hồ sơ riêng"]
  P50_05["P50-05: Local actionhistory và expiry30days"]
  P50_06["P50-06: Bộ cài và startup opt-in"]
  P50_07["P50-07: Own update check/download/install confirmation"]
  P50_08["P50-08: Uninstall giữ/xóa và manualexport reminder"]
 end
 subgraph P60["P60"]
  P60_01["P60-01: Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng"]
  P60_02["P60-02: Hồi quy hai mức và toàn bộ nghiệp vụ"]
  P60_03["P60-03: Phiên8h/offline và ma trận cấu hình"]
  P60_04["P60-04: Rà độc lập, thương hiệu và release gate"]
  P60_05["P60-05: Chuẩn bị công bố và hỗ trợ có kiểm soát"]
 end
 P00_01 --> P00_02
 P00_01 --> P00_03
 P00_01 --> P00_04
 P00_01 --> P01_01
 P00_02 --> P02_01
 P00_04 --> P02_01
 P02_01 --> P02_02
 P02_02 --> P02_03
 P02_01 --> P02_04
 P00_02 --> P02_04
 P02_04 --> P02_05
 P02_03 --> P02_05
 P00_04 --> P03_01
 P03_01 --> P03_02
 P01_01 --> P03_02
 P03_02 --> P03_03
 P02_04 --> P03_03
 P03_03 --> P03_04
 P00_03 --> P03_04
 P00_02 --> P10_01
 P01_01 --> P10_01
 P10_01 --> P10_02
 P02_03 --> P10_02
 P10_02 --> P10_03
 P10_03 --> P10_04
 P10_03 --> P10_05
 P50_01 --> P10_05
 P10_03 --> P10_06
 P00_04 --> P10_06
 P10_01 --> P10_07
 P02_05 --> P10_07
 P00_04 --> P20_01
 P20_01 --> P20_02
 P02_03 --> P20_02
 P02_05 --> P20_02
 P20_02 --> P20_03
 P30_02 --> P20_03
 P20_02 --> P20_04
 P30_01 --> P20_04
 P20_02 --> P20_05
 P02_02 --> P20_05
 P00_02 --> P30_01
 P50_01 --> P30_01
 P30_01 --> P30_02
 P30_02 --> P30_03
 P30_04 --> P30_03
 P50_01 --> P30_04
 P10_01 --> P30_04
 P30_04 --> P30_05
 P10_02 --> P30_05
 P30_03 --> P30_06
 P03_04 --> P30_06
 P02_04 --> P40_01
 P50_01 --> P40_01
 P40_01 --> P40_02
 P10_01 --> P40_02
 P10_03 --> P40_03
 P40_01 --> P40_03
 P50_01 --> P40_03
 P40_03 --> P40_04
 P10_07 --> P40_04
 P20_02 --> P40_04
 P40_04 --> P40_05
 P30_03 --> P40_05
 P03_03 --> P40_06
 P10_03 --> P40_06
 P30_02 --> P40_06
 P20_04 --> P40_06
 P40_05 --> P40_07
 P40_06 --> P40_07
 P10_06 --> P40_07
 P00_02 --> P50_01
 P00_04 --> P50_01
 P50_01 --> P50_02
 P10_01 --> P50_02
 P50_01 --> P50_03
 P00_04 --> P50_03
 P50_03 --> P50_04
 P50_02 --> P50_04
 P50_01 --> P50_05
 P00_04 --> P50_06
 P40_01 --> P50_06
 P20_05 --> P50_06
 P50_06 --> P50_07
 P50_04 --> P50_07
 P50_06 --> P50_08
 P50_03 --> P50_08
 P40_01 --> P60_01
 P20_02 --> P60_01
 P30_02 --> P60_01
 P10_03 --> P60_01
 P60_01 --> P60_02
 P30_06 --> P60_02
 P40_07 --> P60_02
 P50_04 --> P60_02
 P50_05 --> P60_02
 P60_02 --> P60_03
 P03_04 --> P60_03
 P60_03 --> P60_04
 P50_07 --> P60_04
 P50_08 --> P60_04
 P00_04 --> P60_04
 P60_04 --> P60_05
```
