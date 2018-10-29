#!/bin/bash

# ó: 9b -> f3
# í: ad -> ed
# ç: d8 -> e7
# á: ff -> e1
function replaceByte() {
    sed -i "s/\x9b/\xf3/g" "$1"
    sed -i "s/\xad/\xed/g" "$1"
    sed -i "s/\xd8/\xe7/g" "$1"
    sed -i "s/\xff/\xe1/g" "$1"
}

#9b
replaceByte shackleton-s/all_documents/1560.
replaceByte shackleton-s/all_documents/2856.
replaceByte shackleton-s/all_documents/2374.
replaceByte shackleton-s/notes_inbox/1701.
replaceByte shackleton-s/stack__shari/3.
replaceByte campbell-l/all_documents/1014.
replaceByte campbell-l/discussion_threads/889.
replaceByte campbell-l/notes_inbox/284.
replaceByte taylor-m/all_documents/2813.
replaceByte taylor-m/all_documents/7852.
replaceByte taylor-m/notes_inbox/1149.
replaceByte taylor-m/notes_inbox/2425.
replaceByte taylor-m/archive/8_00/32.
replaceByte dasovich-j/all_documents/29349.
replaceByte dasovich-j/notes_inbox/11527.
replaceByte haedicke-m/all_documents/2313.
replaceByte haedicke-m/notes_inbox/344.
replaceByte skilling-j/all_documents/385.
replaceByte skilling-j/discussion_threads/306.
replaceByte skilling-j/notes_inbox/100.

# ad
replaceByte horton-s/all_documents/64.
replaceByte horton-s/all_documents/209.
replaceByte horton-s/discussion_threads/60.
replaceByte horton-s/discussion_threads/198.

#d8
replaceByte sanders-r/all_documents/7334.
replaceByte sanders-r/all_documents/7342.
replaceByte sanders-r/all_documents/7328.
replaceByte sanders-r/notes_inbox/312.
replaceByte sanders-r/notes_inbox/313.
replaceByte sanders-r/notes_inbox/315.
replaceByte griffith-j/all_documents/565.
replaceByte griffith-j/discussion_threads/535.
replaceByte griffith-j/design/27.

#ff
replaceByte taylor-m/all_documents/3452.
replaceByte taylor-m/all_documents/3474.
replaceByte taylor-m/notes_inbox/1606.
replaceByte taylor-m/notes_inbox/1591.
replaceByte gay-r/all_documents/82.
replaceByte gay-r/all_documents/59.
replaceByte gay-r/sent/82.
replaceByte gay-r/sent/59.
