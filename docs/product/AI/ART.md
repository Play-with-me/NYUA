# Art / animation production specification

Visual requirements decided; asset list and implementation details below are work proposals until samples approved. No character generated/approved yet. No licensed anime character or unreviewed AssetStore pack may replace the original design.

## 1. Model sheet contract

Adultfemale chibi, dailyclothes, white/silver waistlonghair with sparse straightbangs, redpinkeyes, warmfairskin, roundneck loose palepinksweater, darkgraypleatedabove-kneeskirt, barefoot; wine-redheartclip anatomicallyright. Front view left of image. Base128x128, transparent background. Predominantly human face/body/gait; only fox ears on head, no human ears; silver-white ears with pale-pink inner ears; exactly one silver-white fox tail. No fox muzzle or animal feet. All previous approved appearance remains unchanged. Exact head/bodyratio, palette and facing-angle count open for visualapproval, not silentlyborrow WorkPets spriteformat.

Required review sheet proposal: front/side/back, neutral/cheerful/sleepy/protest pose, consistent silhouette/hairclip across turns. Smallest64 to largest384 including noninteger scale tested. Pixelstyle must survive renderer import/filter settings; skeletal deformation can blur/distort pixel edges, must be approved if used. No automatic choice of skeletal vs framebyframe.

## 2. Activity inventory — production planning, not all final clips

| Group | Basic needed | Advanced addition | Important transitions |
|---|---|---|---|
| Locomotion | Idle/walk/climb/sit/fall/land/stand | Carry tools/route variations | Surface move/remove, drag interrupts |
| Interaction | Clickreaction/petaccept/petavoid/held/release/startle/protest/refusallift/readiness | Deepaffection/reconciliation/romance optin | Modifiermove never throw/hurt |
| Needs | Eat/drink/refusefood/sleep/doze/wake/rest | Ownactivity variety | Moods change consumption, no compulsorycarepunishment |
| Attention | Wave/peek/invite/selfplay | Contextualcuriosity | Shared2attempts/30mincooldown |
| Hobbies | Basiclife only | Readbook/draw/plush/virtualgame/silent singing/blocks | Animationonly, no book/art/game actual output |
| Media | Simplecontextexpression | Sofa/popcorn/sad/excited/cheer silently | Smoothaffect, no flicker, no sound |
| Realaction embodiment | Approach/climb/tool/virtualkeyboard where permitted | Autonomous exploration same vocabulary | Arrival precedes finalhostcheck, no callbackclick |
| Props | Foodtray/individualfoods/putaway/move | Sofa/book/arttools/plush/handheld/blocks | At most5left, clean byanimation |

Clip names/counts/durations/directions are not fixed by this table. Animation manifest must map states to actual clips only after samples; missingclip has explicit fallback pose, not success-labelledfakeactivity.

## 3. Food/props

Six selections: riceball/noodles; fruit/popcorn;milk/fruitjuice. Apple, orange juice and bunny plush are confirmed. Plush colors/details and ladder/tool visuals remain open H08/D-14. No foodcurrency/crafting/paywall. Can select eachcategory independently, dragitem or tray. Define hand/propanchors and carry/eat/collision bounds separately from decorativehair.

## 4. Technical asset handoff

Manifest proposal: assetId/version, filehash, originalsize, pivots, facing/clipmap, anatomicalclipposition, importfiltering, hitzones(head/body/drag/prop), attachmentanchors, safeplaceholder, source/license/author record. These are rendering metadata, not screenpermissionregions. No worldcoordinate in texturepixels without documented transform.

Review at native capture/defaultDPI and chosenmonitors; enginepreview alone doesn't prove desktopquality. Asset changes can alter hitbox and need gesture regression. Keep sourceart separate from distributedruntimefiles; retain provenance and permitted modifications.

## 5. Acceptance

AT-NV01–06 plus E01; user explicitly approves sample/silhouette/motion. TEAM tracks approvalrevision. Don't create full animationlibrary before standing/movement/gesture sample accepted, and don't mark an AI-generated sprite officially approved from technical size check alone.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **NV01:** D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- **NV02:** D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- **NV11:** D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- **SH04:** D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
