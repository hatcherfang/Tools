# 1.filename "convertClassToInlineStyle.py"  
## 1.1 function introduce:  
>Using regular expression to replace string.  
>>Details: replace all the 'class="xxx"' with the style content.  
>>for example:  
>>>>run command `"python convertClassToInlineStyle.py ./example.html"` and you can get the example.html.rep file. You can diff the two files between example.html and example.html.rep. Finally, you can find all the 'class="xxx"' was replaced by the inline style.
# 2.filename "batchRename.py"
## 2.1 function introduce:
>To batch replace filename as "\*.rep" to "\*".
>>for example:
>>>>directory tree testDir as below:
>>>>>>testDir
>>>>>>├── test1.txt.rep
>>>>>>├── test2.txt.rep
>>>>>>└── test3.txt.rep
>>>>Then you run the command `"python batchRename.py ./testDir"`. It will rename all the file from "test\*.txt.rep" to "test\*.txt".Then you can see the rename result as below:
>>>>>>testDir
>>>>>>├── test1.txt
>>>>>>├── test2.txt
>>>>>>└── test3.txt
# 3.filename "regularReplace.py"
## 3.1 function introduce:
>Using regular expression to batch replace string rA="xxx" with string rB="yyy".
>>for example:
>>>>directory tree testDir as below:
>>>>>>testDir
>>>>>>├── test1.txt
>>>>>>├── test2.txt
>>>>>>└── test3.txt
>>>>all the test\*.txt file content is as below:
>>>>`AAAddsfagagaAAAfaga  AAAddsfagagaAAAfaga  AAAddsfagagaAAAfag  AAAddsfagagaAAAfaga`
>>>>Then you can update variable such as: rA="AAA", rB="BBB" in file "regularReplace.py" to replace all the "AAA" with "BBB" in all of the files under the testDir. Then run the command `"python regularReplace.py ./testDir/"`. All the string "AAA" replaced by "BBB" and saved into file as test\*.txt.rep the tree testDir as below:
>>>>>>testDir
>>>>>>├── test1.txt
>>>>>>├── test1.txt.rep
>>>>>>├── test2.txt
>>>>>>├── test2.txt.rep
>>>>>>└── test3.txt
>>>>>>└── test3.txt.rep
>>>>You can see the files test\*.txt.rep that all the string "AAA" was replaced by "BBB" the content as below:
>>>>`BBBddsfagagaBBBfaga  BBBddsfagagaBBBfaga  BBBddsfagagaBBBfag  BBBddsfagagaBBBfaga`
>>>>Then you can using batchRename.py to rename all the files "test\*.txt.rep" to "test\*.txt".
