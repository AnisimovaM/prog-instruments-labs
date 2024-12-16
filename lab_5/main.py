from NIST_tests import *
from work_with_files import *

if __name__ == "__main__":
   settings = read_json_from_file("settings.json")

   sequences = read_json_from_file(settings["generated_sequences"])
   sequences_cpp = sequences["cpp_generator"]
   sequences_java = sequences["java_generator"]

   nist_frequency_bit_test(sequences_cpp, settings["result_of_tests"], "C++")
   nist_frequency_bit_test(sequences_java, settings["result_of_tests"], "Java")
   
   nist_identical_serial_bits(sequences_cpp, settings["result_of_tests"], "C++")
   nist_identical_serial_bits(sequences_java, settings["result_of_tests"], "Java")  

   nist_longest_sequence(sequences_cpp, settings["result_of_tests"], "C++")
   nist_longest_sequence(sequences_java, settings["result_of_tests"], "Java")

   print('Successful work!')