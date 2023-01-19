print("🌟Website Rating🌟")
print()
web = input("Input website name: ")
url = input("Input the URL: ")
description = input("Input your description: ")
rating = input("Input the star rating out of 5: ")

webRating = {"web": web, "url": url, "description": description, "rating": rating}
print()
for name, value in webRating.items():
  print(f"{name}: {value}")