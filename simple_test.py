def read_chapter_file(chapter_file):
    chapters_list = []
    try:
        with open(chapter_file, 'r') as file:
            for line in file:
                chapters_list.append(line)
            return chapters_list
    except Exception as e:
        print(f"Failed to read file '{chapter_file}': {e}")
        raise


def write_chapters_file(chapter_list, file_name):
    try:
        with open(file_name, 'w') as file:
            for chapter in chapter_list:
                file.write(chapter + '\n\n')
    except Exception as e:
        print(f"Failed to write file: {e}")
        raise


def generate_chapter_list(list_of_chapters, split_chapter_index, split_chapter_name):
    chapter_pattern = '## <a name="{chapter_index}"></a>{chapter_name}'
    sub_chapter_pattern = '### <a name="{sub_chapter_index}"></a>{chapter_name}'
    sub_chapter_part_pattern = '#### <a name="{sub_chapter_index}"></a>{chapter_name}'
    list_of_generated_chapters = []
    for chapter in list_of_chapters:
        chapter_index = chapter.split(split_chapter_index)[1].replace(')', '').replace('\n', '')
        chapter_name = chapter.split(split_chapter_index)[0].split(split_chapter_name)[1].replace(']', '').replace('\n', '')
        if chapter_index.find('part') != -1:
            if chapter_index.startswith('.') != -1:
                list_of_generated_chapters.append(sub_chapter_part_pattern
                                                  .replace('{sub_chapter_index}', chapter_index)
                                                  .replace('{chapter_name}', chapter_name))
            else:
                list_of_generated_chapters.append(sub_chapter_pattern
                                                  .replace('{sub_chapter_index}', chapter_index)
                                                  .replace('{chapter_name}', chapter_name))
        else:
            list_of_generated_chapters.append(chapter_pattern
                                              .replace('{chapter_index}', chapter_index)
                                              .replace('{chapter_name}', chapter_name))
    return list_of_generated_chapters


chapters_list = read_chapter_file('chapters_example.txt')
write_chapters_file(generate_chapter_list(chapters_list, '(#', '['),'output.txt')
