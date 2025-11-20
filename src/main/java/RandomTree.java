import java.util.Random;

/**
 * A utility class to generate and display a random binary tree.
 * This is a Java refactoring of the original Python script `randomTree.py`.
 * The tree is generated recursively to a specified depth, with nodes
 * having a random chance of existing.
 * <p>
 * The main method can be run with an optional command-line argument to specify
 * the tree depth. If no argument is provided, a default depth is used.
 *
 * @author Your Name
 * @version 1.0
 */
public final class RandomTree {

    /**
     * A shared Random instance for generating all random numbers.
     * Using a single instance is more efficient and a best practice.
     */
    private static final Random RANDOM = new Random();

    /** The maximum value for a node in the tree (inclusive, starting from 1). */
    private static final int MAX_NODE_VALUE = 100;

    /** The probability (0.0 to 1.0) that a child node will be created. Corresponds to 1.0 - 0.25 from the Python script. */
    private static final double CHILD_CREATION_PROBABILITY = 0.75;

    /** The default depth of the tree if not specified by the user. */
    private static final int DEFAULT_DEPTH = 4;

    /**
     * Private constructor to prevent instantiation of this utility class.
     */
    private RandomTree() {
        // This class is not meant to be instantiated.
    }

    /**
     * Represents a node in the binary tree.
     * This is a public static nested class as it is a core part of the public API
     * of RandomTree (returned by randomTree and passed to printTree) but is
     * logically grouped within it.
     */
    public static class Node {
        /** The integer value stored in the node. */
        int value;
        /** A reference to the left child node. */
        Node left;
        /** A reference to the right child node. */
        Node right;

        /**
         * Constructs a new Node with a given value.
         *
         * @param value The integer value for this node.
         */
        public Node(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        /**
         * Returns a string representation of the node.
         *
         * @return A string in the format "Node(value)".
         */
        @Override
        public String toString() {
            return "Node(" + value + ")";
        }
    }

    /**
     * Recursively generates a random binary tree of a given maximum depth.
     * <p>
     * Each potential child node has a fixed probability of being created. This can
     * result in trees that are sparse and may not reach the full specified depth
     * on all branches.
     *
     * @param depth The maximum depth of the tree to generate. If non-positive, returns null.
     * @return The root node of the generated binary tree, or {@code null} if depth is 0 or less.
     */
    public static Node randomTree(int depth) {
        if (depth <= 0) {
            return null;
        }

        // Create the root node with a random value between 1 and MAX_NODE_VALUE.
        Node root = new Node(RANDOM.nextInt(MAX_NODE_VALUE) + 1);

        // With a certain probability, create a left child.
        if (RANDOM.nextDouble() < CHILD_CREATION_PROBABILITY) {
            root.left = randomTree(depth - 1);
        }

        // With a certain probability, create a right child.
        if (RANDOM.nextDouble() < CHILD_CREATION_PROBABILITY) {
            root.right = randomTree(depth - 1);
        }

        return root;
    }

    /**
     * Prints the structure of a binary tree to the console in a human-readable format.
     * This is a convenience wrapper for the recursive print method.
     *
     * @param root The root node of the tree to print. If null, a message indicating an empty tree is printed.
     */
    public static void printTree(Node root) {
        if (root == null) {
            System.out.println("Tree is empty.");
            return;
        }
        printTreeRecursive(root, 0, "Root:");
    }

    /**
     * Recursively prints the tree structure, accurately replicating the Python script's output format.
     * It prints placeholders for null children only if their sibling exists, making the structure clearer.
     *
     * @param node   The current node to print.
     * @param level  The current depth level of the node, used for indentation.
     * @param prefix The prefix to display before the node's value (e.g., "Root:", "L---", "R---").
     */
    private static void printTreeRecursive(Node node, int level, String prefix) {
        if (node == null) {
            return;
        }

        // Print the current node with indentation.
        System.out.println(" ".repeat(level * 4) + prefix + " " + node.value);

        // Stop if this is a leaf node.
        if (node.left == null && node.right == null) {
            return;
        }

        String childIndent = " ".repeat((level + 1) * 4);

        // Handle the left child.
        if (node.left != null) {
            printTreeRecursive(node.left, level + 1, "L---");
        } else if (node.right != null) {
            // If left is null but right exists, print a placeholder for clarity.
            System.out.println(childIndent + "L--- null");
        }

        // Handle the right child.
        if (node.right != null) {
            printTreeRecursive(node.right, level + 1, "R---");
        } else if (node.left != null) {
            // If right is null but left exists, print a placeholder for clarity.
            System.out.println(childIndent + "R--- null");
        }
    }

    /**
     * The main entry point for the application.
     * <p>
     * Generates a random tree and prints it to the console.
     * An optional command-line argument can be provided to specify the tree depth.
     * If no argument is given, a default depth is used.
     *
     * @param args Command-line arguments. The first argument, if present, is parsed as the tree depth.
     */
    public static void main(String[] args) {
        int depth = DEFAULT_DEPTH;

        if (args.length > 0) {
            try {
                depth = Integer.parseInt(args[0]);
                if (depth < 0) {
                    System.err.println("Error: Depth cannot be negative. Using default depth " + DEFAULT_DEPTH + ".");
                    depth = DEFAULT_DEPTH;
                }
            } catch (NumberFormatException e) {
                System.err.println("Error: Invalid number format for depth '" + args[0] + "'. Using default depth " + DEFAULT_DEPTH + ".");
                // depth remains DEFAULT_DEPTH
            }
        }

        System.out.println("Generating a random tree with maximum depth: " + depth);
        Node tree = randomTree(depth);

        System.out.println("\nGenerated Random Tree:");
        printTree(tree);
    }
}