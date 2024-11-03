import re

def review(password):
    score = 0
    

    weak_words = [
    "password",
    "123456",
    "qwerty",
    "12345678",
    "12345",
    "123456789",
    "football",
    "1234",
    "1234567",
    "baseball",
    "welcome",
    "1234567890",
    "abc123",
    "111111",
    "1qaz2wsx",
    "dragon",
    "master",
    "monkey",
    "letmein",
    "login",
    "princess",
    "qwertyuiop",
    "solo",
    "passw0rd",
    "starwars",
    "admin",
    "iloveyou",
    "123123",
    "welcome1",
    "admin123",
    "123qwe",
    "trustno1",
    "hello",
    "computer",
    "killer",
    "asdfgh",
    "shadow",
    "access",
    "master",
    "football",
    "superman",
    "696969",
    "batman",
    "1q2w3e4r",
    "test",
    "letmein",
    "love",
    "1234qwer",
    "123456a",
    "hello",
    "666666",
    "qwerty123",
    "samsung",
    "1qazxsw2",
    "charlie",
    "zxcvbn",
    "555555",
    "7777777",
    "welcome1",
    "1234abcd",
    "ashley",
    "football",
    "123456789a",
    "sunshine",
    "qwertyuiop",
    "password1",
    "654321",
    "superman",
    "iloveyou",
    "1q2w3e4r5t",
    "123123",
    "admin",
    "password123",
    "welcome123",
    "princess",
    "abc123",
    "admin123",
    "trustno1",
    "123456a",
    "qwerty123",
    "password1",
    "welcome1",
    "letmein123",
    "password123",
    "iloveyou123",
    "adminadmin",
    "admin1234",
    "password1234",
    "password!",
    "welcome123",
    "football123",
    "password!",
    "123456789!",
    "adminadmin",
    "admin1234",
    "123456789a!",
    "iloveyou123",
    "adminadmin123",
    "admin123456",
    "qwertyuiop123",
    "123456qwerty",
    "123qwe!@#",
    "123qwe!@#",
    "123qwe!@#",
    "letmein!@#",
    "password!@#",
    "welcome!@#",
    "football!@#",
    "admin!@#",
    "abc123!@#",
    "123456a!@#",
    "qwerty123!@#",
    ]
    if password.lower() in weak_words:
        return 0
    
    # Length check
    score += min(len(password) // 4, 4)
    
    # Uppercase and lowercase letters check
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 2
    
    # Numbers check
    if any(c.isdigit() for c in password):
        score += 2
    
    # Special characters
    if any(c in "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~" for c in password):
        score += 2
    
    # Consecutive characters
    if re.search(r'(.)\1\1', password) is None:
        score += 2
    
    # Check for sequential characters
    sequential_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if not any(password[i:i+3] in sequential_chars for i in range(len(password) - 2)):
        score += 2
    
    # Cap the score at 10
    score = min(score, 10)
    
    return score