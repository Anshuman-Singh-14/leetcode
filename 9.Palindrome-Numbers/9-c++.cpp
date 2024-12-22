class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
    std::string s = std::to_string(x);
    return s == std::string(s.rbegin(), s.rend());
    }
};