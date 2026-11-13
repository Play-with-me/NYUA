# Business rules và state invariants

Trạng thái: phân tích từ yêu cầu đã chốt; thuật toán/mức định lượng chưa được chọn đánh dấu D-xx. Các quy tắc không thay nội dung nguồn trong registry.

## 1. Authorization predicates

`readEligible = observing AND visibleCharacter AND sourceVisible AND allowedAppRead AND (notWeb OR allowedSiteRead) AND notPrivate AND safeRegionsKnown AND notSafetyHoldExceptExplicitRetry`.

Tự ẩn không chỉ visibleCharacter=false trên renderer: host phải dừng đọc/control. Khi manual observation off, geometry-only vẫn được phép; không gọi readEligible để tự cấp nội dung cho geometry consumer.

`controlEligible` cần readEligible, app/site control, control enabled, target/action allowed, target identity current, input condition satisfied và không có stop generation mới. Website permission gồm subdomain đúng identity boundary, không substring URL. Domain normalization phải được kiểm chứng trước code thật.

Mặc định mới tắt. Bật control không tự bật read. Thu hồi nguồn chặn truy cập mới ngay; xử lý ký ức giữ/xóa là một workflow riêng, không trì hoãn chặn để chờ user chọn.

## 2. Precedence

1. Không bypass protected/private/sensitive hoặc tác vụ cấm.
2. Emergency/hidden/observation-off/lock làm vô hiệu action theo đúng phạm vi.
3. Human input thắng action đang chờ; explicit request exception chỉ bỏ chờ 60 giây lúc bắt đầu, không bỏ human input tiếp theo.
4. Permission/source/target validity được kiểm lại tại use time.
5. Media-preservation và task prerequisites.
6. Priority requested-job trước autonomous exploration; một lần delay do mood không mở rộng grant.
7. Mood/preferences quyết định cách biểu hiện và chọn hoạt động đủ quyền còn lại.

Không dùng một integer priority đơn lẻ thay toàn bộ predicate: emergency và deny là ràng buộc, không chỉ task ưu tiên cao.

## 3. Lifecycle matrix

| Event | Content | Control | Body | Running job | Not-started jobs | Resume |
|---|---|---|---|---|---|---|
| Human input | Theo quyền | Yield | Vẫn sinh hoạt | Yielded | Eligible sau idle | 60s idle + revalidate |
| Emergency | Theo quyền | Off | Vẫn sinh hoạt | Cancelled | Paused | User enable + ResumeQueue |
| ObservationOff | Off | Off | Geometry-only | Cancelled | Paused | User enable + ResumeQueue |
| ManualHide | Off | Off | Hidden all props | Cancelled | Paused | Show + ResumeQueue |
| RelationshipHide | Off | Off | Private state only | Cancelled | Paused | Voluntary return + ResumeQueue |
| ControlledExit | Off | Off | Not running | Cancelled after warning | Cancelled after warning | Never auto restore queue |
| ProfileSwitch | Old off | Old off | Old frozen | Cancelled after warning | Cancelled after warning | New profile starts independent |

Job error: FailedNeedsTeaching tại bước lỗi; không tự retry từ đầu. Queue scheduler xem việc sau độc lập; không assume postcondition của job lỗi. Terminal job không tự trở lại Running sau reconnect/ResumeQueue.

## 4. Time semantics

- Active input: chuột/phím người thật, không nội dung phím. Idle gate 60s, autonomous media gate default5m adjustable; timers không được lấy từ injected input.
- Neglect accumulates only advanced+visible+selectedProfile+humanActive. Sau60s idle stop counting. Trust/hurt maps threshold48–72h; mapping function chưa chốt (D-05).
- Intentional click/pet/feed ngắt streak, không xóa accumulated sadness. Offline không tăng neglect. Inactive profile freezes mọi state; app closed của active profile có elapsed-state reconciliation, không invent events.
- Human unlock input không reset idle timer; desktop input kế tiếp reset. Sleep duration không được coi là humanActive; thời gian sleep có cộng vào 5m chờ media hay không ngoài case khóa máy còn cần xác định D-11.
- Invitation and attention-seeking tease share2 attempts then cooldown>=30min; interval giữa hai lần rủ chưa chốt D-05.
- Movie taste>=20min + user selection/transition evidence; music repeated/similar songs + user navigation evidence. Không suy ra continuous presence hoặc grant background-reading.
- Log retention30days khác memory decay importance/reinforcement. Memory decay không dùng fixed TTL.

## 5. Memory/relationship operations

| Operation | Content | Contribution/relationship | Scope |
|---|---|---|---|
| Edit memory | Thay thông tin | Không tính lại | Current profile |
| Explicit delete | Xóa | Điều chỉnh phần từng ảnh hưởng, đúng một lần | Current profile/source selected |
| Natural fade | Quên chi tiết | Giữ closeness | Unpinned, importance based |
| Pin/unpin | Không sửa nội dung | Pin chống fade, không tự tăng relation | Current profile |
| Romance off, retain | Giữ romantic memories | Buồn tạm, tôn trọng; không tự bật | Advanced expression off |
| Reset | Xóa memory, state, relation, lessons | Khởi tạo lại | Current only; global grants giữ |

Xóa romantic memories phải dùng semantics explicit-delete, không bỏ qua contribution vì khác màn hình. Recovery code/password reset backup không có server giúp nếu cả hai mất; app không hứa khôi phục được.

## 6. Media và learning

Tự media chỉ advanced, idle đủ, unlocked, không media đang phát, allowedBrowser+site; dùng tab riêng và browser user chọn. Không tự đổi app/window để nghịch; task điều hướng hợp lệ có thể focus trong quyền khi humanIdle. Hai trường hợp khác mục đích.

Demo chỉ active khi user bật, cùng app/site; review before save. New search text là input parameter cho ô search/navigation. Result target chọn rõ first-result hoặc identity; không suy ra “bấm dòng đầu” từ một tọa độ.

Denied login/pay/verification → tìm nội dung free khác, tối đa3 candidates per search session. Định nghĩa search session/cooldown sau ba lần cần chốt D-06 để không reset bộ đếm liên tục.

## 7. Mô hình trạng thái nhiều chiều

Không gộp tất cả vào enum Sleep/Play/Hidden duy nhất. Tách lifecycle (app/profile), mode, observation/control, body activity, mood/relationship, job/queue. Ví dụ cô ấy ngủ vẫn có thể visible; không đồng nghĩa tắt quan sát nếu chưa có quy tắc; người dùng cần làm rõ dữ liệu quan sát lúc ngủ trước triển khai D-12.

Các state chart trong diagrams thể hiện một chiều, không phải cross-product hoàn chỉnh. Kiểm tra forbidden combinations: hidden+reading, control-without-read, inactive-profile+time-progress, cancelled-job+auto-replay.
