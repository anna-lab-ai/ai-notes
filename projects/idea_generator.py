# Idea Generator AI (simple version)

def generate_ideas(topic):
    ideas = [
        f"{topic} app",
        f"{topic} automation tool",
        f"{topic} daily assistant",
        f"{topic} tracker",
        f"{topic} smart system"
    ]
    return ideas


# ---- RUN ----
topic = input("Enter topic: ")

result = generate_ideas(topic)

print("\nGenerated ideas:\n")
for i, idea in enumerate(result, 1):
    print(f"{i}. {idea}")
