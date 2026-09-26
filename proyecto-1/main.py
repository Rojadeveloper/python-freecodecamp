def add_setting(test_settings, setting):
    setting_lower = tuple(x.lower() for x in setting)

    if setting_lower[0] in test_settings:
        return f"Setting '{setting_lower[0]}' already exists! Cannot add a new setting with this name."
    else:
        test_settings.update((setting_lower,))
        return f"Setting '{setting_lower[0]}' added with value '{setting_lower[1]}' successfully!"


def update_setting(test_settings, setting):
    setting_lower = tuple(x.lower() for x in setting)

    if setting_lower[0] in test_settings:
        test_settings.update({setting_lower[0]: setting_lower[1]})
        return f"Setting '{setting_lower[0]}' updated to '{setting_lower[1]}' successfully!"
    else:
        return f"Setting '{setting_lower[0]}' does not exist! Cannot update a non-existing setting."


def delete_setting(test_settings, key):
    key = key.lower()

    if key in test_settings:
        test_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    else:
        return "Current User Settings:\n" + "\n".join(
            f"{x.capitalize()}: {value}"
            for x, value in test_settings.items()
        ) + "\n"


test_settings = {
    "theme": "light"
}

print(view_settings({
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}))
