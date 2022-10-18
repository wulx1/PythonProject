student = [{"sno":101,"sname":"小张"," grade":86},
           {"sno":102,"sname":"小王"," grade":96},
           {"sno":103,"sname":"小李"," grade":89},
           {"sno":104,"sname":"小赵"," grade":99}]

student_list = sorted(student, key=lambda x: x["grade"])
print(student_list)





