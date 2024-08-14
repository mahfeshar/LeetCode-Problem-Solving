class Solution {
public:
    bool wordPattern(string pattern, string s) {
        map<char, string> mp;
        vector<string> str;
        string word = \\;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ' && word != \\) {
                str.push_back(word);
                word = \\;
                continue;
            }
            word += s[i];
        }
        if (word != \\)
            str.push_back(word);
        if (str.size() != pattern.size())
            return false;
        for (int i = 0; i < str.size(); i++) {
            auto it = mp.find(pattern[i]);
            if (it == mp.end()) {
                mp[pattern[i]] = str[i];
                for (auto j: mp){
                    if(j.first != pattern[i] && j.second == str[i])
                        return false;
                }
            } 
            else if (it->second != str[i])
                return false;
        }
        return true;
    }
};