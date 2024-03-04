tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#Unión
merged_tags = tags_one | tags_two
print(merged_tags) #Une ambos sets e incluye aquellos elementos únicos

#Tags que están en 'tag_one' pero no en 'tag_two'
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

#Tags que están compartidos en 'tag_one' y en 'tag_two'
shared_tags = tags_one & tags_two
print(shared_tags)
