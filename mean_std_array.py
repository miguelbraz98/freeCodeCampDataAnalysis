import numpy as np

def mean_std_dev(array):
    try:
        #turn into 3x3 and create final dictionary
        np_array = np.array(array).reshape(3,3)
        results = {'mean': [],
                   'variance': [],
                   'standard deviation': [],
                   'max': [],
                   'min': [],
                   'sum': []
                   }

        #test print
        print (np_array)
        #mean calculation

        axis_1 = np.mean(np_array, axis=0)
        axis_2 = np.mean(np_array, axis=1)
        flattened = np.mean(np_array.flatten())
        results['mean'] = [list(axis_1), list(axis_2), flattened]

        #variance calculation
        axis_1 = np.var(np_array, axis=0)
        axis_2 = np.var(np_array, axis=1)
        flattened = np.var(np_array.flatten())
        results['variance'] = [list(axis_1), list(axis_2), flattened]
        #STANDARD DEVIATION CALCULATION

        axis_1 = np.std(np_array, axis=0)
        axis_2 = np.std(np_array, axis=1)
        flattened = np.std(np_array.flatten())
        results['standard deviation'] = [list(axis_1), list(axis_2), flattened]

        #MAX

        axis_1 = np.max(np_array, axis=0)
        axis_2 = np.max(np_array, axis=1)
        flattened = np.max(np_array.flatten())
        results['max'] = [list(axis_1), list(axis_2), flattened]

        #MIN

        axis_1 = np.min(np_array, axis=0)
        axis_2 = np.min(np_array, axis=1)
        flattened = np.min(np_array.flatten())
        results['min'] = [list(axis_1), list(axis_2), flattened]

        #SUM

        axis_1 = np.sum(np_array, axis=0)
        axis_2 = np.sum(np_array, axis=1)
        flattened = np.sum(np_array.flatten())
        results['sum'] = [list(axis_1), list(axis_2), flattened]

    except:
        raise ValueError("List must contain nine numbers.")
mean_std_dev([0,1,2,3,4,5,6,7,8,])