
def reverse(s: str) -> str:
    words = s.split()               
    reversed_words = [w[::-1] for w in words]  
    return " ".join(reversed_words)


if __name__ == "__main__":
    s = "Java from world hello"
    print(reverse(s))
