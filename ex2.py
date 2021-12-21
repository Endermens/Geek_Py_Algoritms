
#  Без использования «Решета Эратосфена»

def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]

 # 3 function calls in 0.000 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.000    0.000 ex2.py:1(<module>)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 #  Используя алгоритм «Решето Эратосфена»


 def sieve(num_list, idx):
     num_list[1] = 0
     i = 2
     s_num_list = []
     while len(s_num_list) < idx:
         if num_list[i] != 0:
             s_num_list.append(num_list[i])
             j = i * 2
             while j < len(num_list):
                 num_list[j] = 0
                 j += i
         i += 1
     return s_num_list[-1]

  # 3 function calls in 0.000 seconds
  #
  #   Ordered by: standard name
  #
  #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #        1    0.000    0.000    0.000    0.000 ex2.py:1(<module>)
  #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
  #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Сложность 1го алгоритма (Перебор)  = O(n**2)     y = 0,1912x**2 + 2,0725x + 5,5545
# Сложность 2го алгоритма (Эратосфен) = O(n**2)    y = 0,2058x**2 - 5,7299x + 24,481
# Сложность алгоритмов объясняется вложенностью циклов.
