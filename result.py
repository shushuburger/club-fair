import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOCAL_FILE = BASE_DIR / "participants.local.txt"
EXAMPLE_FILE = BASE_DIR / "participants.example.txt"


def load_people() -> list[str]:
    source = LOCAL_FILE if LOCAL_FILE.exists() else EXAMPLE_FILE
    if source == EXAMPLE_FILE:
        print("participants.local.txt가 없어 예시 데이터로 실행합니다.")

    lines = source.read_text(encoding="utf-8").splitlines()
    people = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]
    if not people:
        raise ValueError(f"참가자 데이터가 비어 있습니다: {source.name}")
    return people


def main() -> None:
    people = load_people()
    n = 3  # 원하는 인원 수로 변경
    if len(people) < n:
        raise ValueError(f"참가자 수({len(people)})가 추첨 인원 수({n})보다 적습니다.")

    winners = random.sample(people, n)
    print("🎉 커피 쿠폰 당첨자 🎉")
    for winner in winners:
        print("-", winner)


if __name__ == "__main__":
    main()
