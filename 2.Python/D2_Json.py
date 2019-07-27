import json

#str -> Json Obj
json_1row_Str=  '{ "Id":"fcic" ,     "age":30}'
json_1row_Obj = json.loads(json_1row_Str)
#print( json_1row_Obj['age'] )

#Json Obj
json_1row_Obj2 = { "Id":"fcic" ,     "age":30}
#print( json_1row_Obj2['age'] )


json_Nrow_Obj2 = [{ "Id":"fcic" ,     "age":30},{"Id":"ooobbb","age":31} ] 
print( json_Nrow_Obj2[1]['age'] )