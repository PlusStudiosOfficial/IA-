import os

BASE_FILE = "IAbrain.txt"

def load_knowledge():
    knowledge = {}
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                if "=" in line:
                    question, answer = line.strip().split("=", 1)
                    knowledge[question.strip()] = answer.strip()
    return knowledge

def save_knowledge(knowledge):
    with open(BASE_FILE, "w", encoding="utf-8") as file:
        for question, answer in knowledge.items():
            file.write(f"{question} = {answer}\n")

def teach_mode(knowledge):
    print("🧑‍🏫 TEACH MODE: Type 'exit' to finish.")
    while True:
        question = input("Question: ").strip()
        if question.lower() == "exit":
            break
        if question in knowledge:
            print("🤖 I already know that answer. Please ask another question.")
            continue
        answer = input("Answer: ").strip()
        knowledge[question] = answer
        print("✅ Learned.")
    save_knowledge(knowledge)

def answer_mode(knowledge):
    print("🧠 ANSWER MODE: Type 'exit' to finish.")
    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            break
        answer = knowledge.get(question)
        if answer:
            print(f"🤖: {answer}")
        else:
            print("🤖: I don't know the answer... please teach me in TEACH MODE.")

def main_menu():
    knowledge = load_knowledge()
    while True:
        print("\n🧠 Welcome to the AI+ an AI OpenSurce\n")
        print("Options:")
        print("1. Teach the AI")
        print("2. Ask the AI")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            teach_mode(knowledge)
        elif choice == "2":
            answer_mode(knowledge)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
