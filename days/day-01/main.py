import argparse

def main():
    parser = argparse.ArgumentParser(description="Day 01 — Hello CLI")
    parser.add_argument("--name", default="World", help="Your name")
    args = parser.parse_args()
    print(f"Hello, {args.name}! 🎉 You just ran your first #100DaysOfCode Python script.")

if __name__ == "__main__":
    main()
