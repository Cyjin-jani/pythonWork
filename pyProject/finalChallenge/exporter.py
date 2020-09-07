import csv

def save_to_file(word, jobs):
  file = open(f"{word}.csv", mode="w")
  writer =csv.writer(file)
  writer.writerow(["title", "company", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return