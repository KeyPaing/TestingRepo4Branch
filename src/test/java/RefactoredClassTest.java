import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void testLinearSearch_targetFound() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 11, 15));
        int target = 7;
        int expectedIndex = 3;
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);
    }

    @Test
    void testLinearSearch_targetNotFound() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 11, 15));
        int target = 12;
        int expectedIndex = -1;
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);
    }

    @Test
    void testLinearSearch_emptyArray() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>();
        int target = 7;
        int expectedIndex = -1;
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);
    }

    @Test
    void testLinearSearch_targetAtBeginning() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 11, 15));
        int target = 1;
        int expectedIndex = 0;
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);
    }

    @Test
    void testLinearSearch_targetAtEnd() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 11, 15));
        int target = 15;
        int expectedIndex = 6;
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);
    }

    @Test
    void testLinearSearch_duplicateTarget() {
        Solution solution = new Solution();
        List<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 7, 9, 15));
        int target = 7;
        int expectedIndex = 3; // Should return the first occurrence
        int actualIndex = solution.linearSearch(arr, target);
        assertEquals(expectedIndex, actualIndex);

    }



}
