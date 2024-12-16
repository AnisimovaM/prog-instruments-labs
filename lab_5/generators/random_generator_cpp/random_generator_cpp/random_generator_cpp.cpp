
#include <iostream>
#include <random>

/**
 * Generates a random sequence of 0s and 1s.
 *
 * @param randomSequence An array to store the generated random sequence.
 * @param sequenceLength The length of the random sequence to generate.
 */
void random_generator(int randomSequence[], int sequenceLength) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, 1);

    for (int i = 0; i < sequenceLength; ++i) {
        randomSequence[i] = dist(gen);
    }
}

int main() {
    const int sequenceLength = 128;
    int randomSequence[sequenceLength];

    random_generator(randomSequence, sequenceLength);

    for (int i = 0; i < sequenceLength; ++i) {
        std::cout << randomSequence[i];
    }
    std::cout << std::endl;

    return 0;
}
