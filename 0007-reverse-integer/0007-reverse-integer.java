class Solution {
    public int upLim = 2147483647;
    public int lowLim = -2147483648;

    public int reverse(int x) {
        int y = helper(x);
        if (y > upLim || y < lowLim){
            return 0;
        } else{
            return y;
        }
    }

    public int helper(int x) {
        int fin = 0;
        do {
            int curr = x % 10;
            if (fin > upLim / 10 || (fin == upLim / 10 && curr > 7)) {
                return 0;
            }
            else if (fin < lowLim / 10 || (fin == lowLim / 10 && curr < -8)) {
                return 0;
            }
            else{
            fin = fin * 10 + curr;
            x = x / 10; 
            } 
        } while (x != 0);
        return fin;
    }
}