public class Solution {

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {
        int[] solution = new int[a.length];
        for(int i = 0; i < a.length; i++){
            int position = (a.length+(i-d)) % a.length;
            solution[position] = a[i];
        }
        return solution;
    }