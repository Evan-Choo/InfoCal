import similarity
import proportion
import frequency


S_FILE_PATH = r'/Users/EvanChoo/Downloads/vectorFiles/2008-2012.xlsx'
P_FILE_PATH = r'/Users/EvanChoo/Downloads/frequencyFiles/2008-2012.xlsx'

similarity.FILE_PATH = S_FILE_PATH
s_matrix = similarity.calculate_similarity()
diff_matrix = similarity.calculate_difference()

d_matrix = proportion.calculate_proportion(P_FILE_PATH, diff_matrix)

s = frequency.calculate_s(P_FILE_PATH)
print s










