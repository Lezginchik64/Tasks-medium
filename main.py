password = input()
print("YES" if all([any(i.isupper() for i in password), any(i.islower() for i in password),
                    any(i.isdigit() for i in password), len(password) >= 7]) else 'NO')
