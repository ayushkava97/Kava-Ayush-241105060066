print("Hotel Feedback")

hotels = ["A", "B", "C"]
feedbacks = []

for i in range(3):   # Missing colon fixed
    fb = input("Enter feedback: ")
    feedbacks.append(fb)

print("Feedbacks:", feedbacks)   # Correct variable name

if len(feedbacks) > 0:   # Missing colon fixed
    print("Recorded")
else:   # Missing colon fixed
    print("No feedback")

for i in range(2):   # Missing colon fixed
    print("Done")

print("End")