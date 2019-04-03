def init(registry):
	registry.register_operator("test.operator","Test operator",
		lambda: print("Running operator"))