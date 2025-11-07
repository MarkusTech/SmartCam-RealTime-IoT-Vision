def handle_command(command):
    if command == "turn-on-light":
        return "💡 Light turned ON"
    elif command == "turn-off-light":
        return "💡 Light turned OFF"
    else:
        return "❌ Unknown command"
