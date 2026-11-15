extends SceneTree
# Isolated B00-02 GDScript headless smoke script.
# Invoked via: Godot --headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --quit
# NOTE: Does NOT prove C# compilation, Windows Desktop export, DWM transparency, click-through, IPC, or NV08.

func _init() -> void:
	var user_args: PackedStringArray = OS.get_cmdline_user_args()

	if user_args.has("--probe-neg"):
		printerr("[NYUA-B00-02] Deliberate negative control (--probe-neg) -> exit 1.")
		quit(1)
		return

	if user_args.has("--probe-hang"):
		print("[NYUA-B00-02] Entering deliberate hang (--probe-hang) for UW02 supervisor kill-tree check...")
		while true:
			OS.delay_msec(1000)
		return

	var packed: Resource = ResourceLoader.load("res://scenes/Bootstrap.tscn")
	if packed == null or not (packed is PackedScene):
		printerr("[NYUA-B00-02] Failed to load PackedScene res://scenes/Bootstrap.tscn.")
		quit(2)
		return

	var instance: Node = (packed as PackedScene).instantiate()
	if instance == null:
		printerr("[NYUA-B00-02] Failed to instantiate res://scenes/Bootstrap.tscn.")
		quit(3)
		return

	if not instance.has_node("SyntheticPlaceholder"):
		printerr("[NYUA-B00-02] Missing expected SyntheticPlaceholder node.")
		instance.free()
		quit(4)
		return

	instance.free()
	print("[NYUA-B00-02] Bootstrap.tscn instantiated OK (positive headless smoke).")
	quit(0)
