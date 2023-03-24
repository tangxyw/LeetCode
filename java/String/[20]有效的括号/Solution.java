import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Solution {
    private static final Map<Character, Character> hashtable = new HashMap<Character, Character>(){
        {
            put(')', '(');
            put(']', '[');
            put('}', '{');
        }
    };

    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<Character>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (hashtable.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != hashtable.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.isValid("[{}]");
        System.out.println(result);
    }
}