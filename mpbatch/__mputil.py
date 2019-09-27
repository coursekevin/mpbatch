import multiprocessing as mp


def batch_process(func, iter_input, num_cores):
    """ Takes in a function, independent inputs to the function in a list, and the number of desired parallel cores
            and parallelizes the computation across the number of cores desired, returning the function answer in a list

            ie. returns func(iter_input) but parallelizes across num_cores

            ARGS:
                    func (function) = function that accepts a variable sized list input and returns the result of each element
                                      of input list in a list of the same dimension
                    iter_input (list) = list of independent function inputs
                    num_cores (int) = number of cores to be parallelized accross

            OUTPUTS:
                    output of func(list) = return of func(iter_input)
    """

    # define function alias to allow for mp
    def __func_alias(iterable, send_end):
        return_val = func(iterable)
        #print('Return val: %s' % return_val)
        send_end.send(return_val)

    # initialization of parallel dictionary to map subprocess to initial input
    parallel_dict = {}
    for core in range(num_cores):
        parallel_dict[core] = []

    # construction of parallel dict. which holds index of inputs and maps them to which core is responsible for output
    core_count = 0
    for idx in range(len(iter_input)):
        parallel_dict[core_count].append(idx)

        core_count += 1
        if core_count == num_cores:
            core_count = 0

    # initialization of multiprocess tracking lists
    proc_list = []
    pipe_list = []

    for core in range(num_cores):

        recv_end, send_end = mp.Pipe(False)
        sub_list = [iter_input[i] for i in parallel_dict[core]]
        args = (sub_list, send_end)
        proc = mp.Process(target=__func_alias, args=args)
        proc_list.append(proc)
        pipe_list.append(recv_end)

        proc.start()

    # wait for processes to finish
    for proc in proc_list:
        proc.join()

    # intialize return list
    return_list = [0 for i in iter_input]
    for core in range(num_cores):
        sub_ans = pipe_list[core].recv()
        for idx, ans in zip(parallel_dict[core], sub_ans):
            return_list[idx] = ans

    return return_list


# define function alias to allow for mp
if __name__ == '__main__':

    # EXAMPLE USAGE
    def test_func(L):
        return [el**2 for el in L]

    test_L = [i+1 for i in range(10000)]

    output = batch_process(test_func, test_L, 4)
    print(output)
