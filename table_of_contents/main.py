

# import os

def tableOfContents(text):
    result = []
    chapter_num = 1
    section_num = 1

    for line in text:
        if line.startswith("# "):
            result.append(f"{chapter_num}. {line[2:]}")
            chapter_num += 1
            section_num = 1
        elif line.startswith("## "):
            result.append(f"   {chapter_num - 1}.{section_num} {line[3:]}")
            section_num += 1

    return result

if __name__ == '__main__':

    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w') # opens file for writing
                                                # the output is the path stored in
                                                # env var named TEST_DIR
    text_count = int(input().strip())
    text = []

    for _ in range(text_count):                 # prompt the user for text input
        item = input()
        text.append(item)
    '''
    text = [
        "# Introduction",
        "## Overview",
        "## Goals",
        "# Chapter 1",
        "## Section 1.1",
        "## Section 1.2",
        "# Chapter 2",
        "## Section 2.1",
    ]

    result = tableOfContents(text)

    for item in result:
        print(item)

    '''
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
    '''

