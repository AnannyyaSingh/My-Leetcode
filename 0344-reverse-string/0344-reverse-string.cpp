class Solution {
public:
    void reverseString(vector<char>& s) {
        //reverse(s.begin(), s.end()); // Using STL

        int left = 0, right = s.size() - 1;
        while( left < right){
           /* swap(s[left], s[right]);
            left++;
            right--; */

        //Manual Swap

        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        s[right] = temp;
        left++;
        right--;
        }
    }
};