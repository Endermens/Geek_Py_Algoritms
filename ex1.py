# я выбрал задание 9  из   3-го  урока
# я нашел такой вот вариант ответа  и привер содержалвесьма избыточную  информацию

import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, line in enumerate(matrix):

    if i == 0:                              # Первую строку копируем для сравнения сразу переходим ко второй строке
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:            # В строках сравниваем каждый элемент с элементом в копии первой строки
            min_line[idx] = item            # меняем по индексу для сохранения порядка
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')

   #       1293 function calls (1266 primitive calls) in 0.003 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:100(acquire)
   #    6/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:1022(_find_and_load)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:125(release)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:165(__init__)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:169(__enter__)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(__exit__)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:179(_get_module_lock)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:198(cb)
   #   10/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
   #     46    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:244(_verbose_message)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:254(_requires_builtin_wrapper)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:357(__init__)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:391(cached)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:404(parent)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:412(has_location)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:421(spec_from_loader)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:48(_new_module)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:492(_init_module_attrs)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:564(module_from_spec)
   #    6/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:664(_load_unlocked)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:71(__init__)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:746(find_spec)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:770(create_module)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:778(exec_module)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:795(is_package)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:826(find_spec)
   #     10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:893(__enter__)
   #     10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:897(__exit__)
   #      6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:921(_find_spec)
   #    6/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:987(_find_and_load_unlocked)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1040(__init__)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1065(get_filename)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1070(get_data)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1089(path_stats)
   #     40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:119(<listcomp>)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:132(_path_split)
   #     12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:134(<genexpr>)
   #     10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1347(_path_importer_cache)
   #      2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:1390(_get_spec)
   #     12    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:140(_path_stat)
   #      2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:1422(find_spec)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:150(_path_is_mode_type)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1522(_get_spec)
   #      8    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1527(find_spec)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:159(_path_isfile)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:172(_path_isabs)
   #      4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:380(cache_from_source)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:510(_get_cached)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:542(_check_name_wrapper)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:585(_classify_pyc)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:618(_validate_timestamp_pyc)
   #      8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:67(_relax_case)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:670(_compile_bytecode)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:721(spec_from_file_location)
   #      6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_unpack_uint32)
   #      2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:874(create_module)
   #    2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap_external>:877(exec_module)
   #      2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:950(get_code)
   #     40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:96(_path_join)
   #      1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
   #      1    0.000    0.000    0.003    0.003 ex9.py:1(<module>)
   #      1    0.000    0.000    0.000    0.000 ex9.py:4(<listcomp>)
   #      1    0.000    0.000    0.001    0.001 random.py:1(<module>)
   #      1    0.000    0.000    0.000    0.000 random.py:103(Random)
   #      1    0.000    0.000    0.000    0.000 random.py:119(__init__)
   #      1    0.000    0.000    0.000    0.000 random.py:128(seed)
   #      1    0.000    0.000    0.000    0.000 random.py:219(__init_subclass__)
   #      9    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
   #      9    0.000    0.000    0.000    0.000 random.py:292(randrange)
   #      9    0.000    0.000    0.000    0.000 random.py:366(randint)
   #      1    0.000    0.000    0.000    0.000 random.py:813(SystemRandom)
   #      2    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
   #     22    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
   #      4    0.000    0.000    0.000    0.000 {built-in method _imp.create_builtin}
   #      4    0.000    0.000    0.000    0.000 {built-in method _imp.exec_builtin}
   #      6    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
   #      2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
   #     22    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
   #     27    0.000    0.000    0.000    0.000 {built-in method _operator.index}
   #     12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
   #     12    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
   #      2    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
   #    3/1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
   #     28    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
   #     29    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
   #     16    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
   #     91    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      4    0.000    0.000    0.000    0.000 {built-in method builtins.max}
   #     18    0.001    0.000    0.001    0.000 {built-in method builtins.print}
   #      6    0.000    0.000    0.000    0.000 {built-in method from_bytes}
   #      2    0.000    0.000    0.000    0.000 {built-in method io.open_code}
   #      2    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
   #      1    0.000    0.000    0.000    0.000 {built-in method math.exp}
   #      2    0.000    0.000    0.000    0.000 {built-in method math.log}
   #      1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
   #      2    0.000    0.000    0.000    0.000 {built-in method nt._path_splitroot}
   #      6    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
   #      2    0.000    0.000    0.000    0.000 {built-in method nt.getcwd}
   #     12    0.001    0.000    0.001    0.000 {built-in method nt.stat}
   #      1    0.000    0.000    0.000    0.000 {function Random.seed at 0x000002563B547AC0}
   #      2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
   #     12    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
   #     44    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      9    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #    132    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
   #     12    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
   #     13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
   #     44    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
   #      6    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
   #      8    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
   #     24    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
   #    124    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
   #     86    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}

   #  потом  я вспомнил про   функцию мап и сделалсвой код минималистичным, таким  как вы вмидели его в 9 задании
   # код выполняет ту же задачу но  за меньшие  ресурсы

   data = [[1, 2, 3], [5, 2, 3], [7, 5, 0]]
   print(max(map(min, data)))

   #  5 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 ex9.py:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

   # как видно навыполнение затрачиваеться значительно  меньше времени и  ресурсов
