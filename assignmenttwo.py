def calculate_cookout_requirements():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs per person: "))

    hot_dogs_per_package = 10
    buns_per_package = 8
    total_hot_dogs = people * hot_dogs_per_person
    hot_dog_packages_needed = (total_hot_dogs + hot_dogs_per_package - 1) // hot_dogs_per_package
    bun_packages_needed = (total_hot_dogs + buns_per_package - 1) // buns_per_package

    leftover_hot_dogs = (hot_dog_packages_needed * hot_dogs_per_package) - total_hot_dogs
    leftover_buns = (bun_packages_needed * buns_per_package) - total_hot_dogs

    print("Requirements for the cookout:")
    print("Hot dog packages needed:", hot_dog_packages_needed)
    print("Bun packages needed:", bun_packages_needed)
    print("Leftover hot dogs:", leftover_hot_dogs)
    print("Leftover buns:", leftover_buns)

calculate_cookout_requirements()