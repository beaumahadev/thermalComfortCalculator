import fangers


#sample values
input_test_1=[27,60,1.1,.5]
input_test_2=[25,40,1.8,.5]
input_test_3=[20,40,1.8, 1]
input_test_4=[24,80,1.8,.2]
input_test_5=[20,40,1.1,.5]


test_inputs=[input_test_1]


#Answers taken from CBE Thermal Comfort Calculator: http://comfort.cbe.berkeley.edu/
test_1_answers=[.62,13]
test_2_answers=[.81,19]
test_3_answers=[-.19,6]
test_4_answers=[.37,8]
test_5_answers=[-1.87,71]

test_answers=[test_1_answers]


def test_fangers(input_array, answer_array):
    answer= fangers.calculate(input_array[0],input_array[1],input_array[2],input_array[3])
    answer_pmv= round(answer['pmv'],2)
    answer_ppd= round(answer['ppd'])
    assert answer_pmv  == answer_array[0], "PMV is: " + str(answer_pmv) + ", should be: "+ str(answer_array[0])
    assert answer_ppd  == answer_array[1], "PPD is: " + str(answer_ppd) + ", should be: "+ str(answer_array[1])


if __name__ == "__main__":
    for i in range(0,len(test_inputs)):
        test_fangers(test_inputs[i],test_answers[i])
    
    print("All tests passed")
