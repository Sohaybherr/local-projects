#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define N 5
#define A 2


int transaction[N][A] = {
    {1,0},
    {2,3},
    {2,2},
    {4,3},
    {2,3},
};
bool finals[N]={false,true,true,true
    ,true};
void affich_automate(FILE *f) {
fprintf(f, "Etat | a | b |Final\n");
for (int i = 0; i < N; i++) {
fprintf(f, " %d   | %d | %d | %s\n", i, transaction[i][0], transaction[i][1], finals[i]?"oui":"non");
}
}
void minimaze_automate(FILE *f) {
    bool distinguishable[N][N] = {false};

    // Mark pairs where one is final and the other is not
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            if (finals[i] != finals[j]) {
                distinguishable[i][j] = true;
            }
        }
    }

    // Iteratively mark distinguishable pairs
    bool changed;
    do {
        changed = false;
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                if (!distinguishable[i][j]) {
                    for (int a = 0; a < A; a++) {
                        int next_i = transaction[i][a];
                        int next_j = transaction[j][a];
                    if(next_i > next_j) {
                        int temp = next_i;
                        next_i = next_j;
                        next_j = temp;
                        }
                        if (distinguishable[next_i][next_j]) {
                            distinguishable[i][j] = true;
                            changed = true;
                            break;
                        }
                    }
                }
            }
        }
    } while (changed);

    // Print equivalent states
    fprintf(f, "Equivalent states:\n");
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (!distinguishable[i][j]) {
                fprintf(f, " q%d ≡ q%d\n", i, j); 
            }
        }
    }
}
int main() {
  FILE *f = fopen("C:\\Users\\SOHAYB\\Documents\\compi_cours\\minimization_output.txt", "w");

    if (!f) {
    perror("Error opening file");
    return 1;
}

    printf("Automate initial:\n");
    affich_automate(f);

    printf("\nAutomate minimisé:\n");
    minimaze_automate(f);
  fclose(f);
    return 0;
}