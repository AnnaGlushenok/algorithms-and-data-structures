public class HaffmanNode {
    private int frequency; //частота
    private String el;//символ
    private HaffmanNode left, right; //правая левая дорожка

    public int getFrequency() {
        return frequency;
    }

    public String getEl() {
        return el;
    }

    public HaffmanNode getLeft() {
        return left;
    }

    public HaffmanNode getRight() {
        return right;
    }

    public void setLeft(HaffmanNode left) {
        this.left = left;
    }

    public void setRight(HaffmanNode right) {
        this.right = right;
    }

    public HaffmanNode(int frequency, String el) {
        this.frequency = frequency;
        this.el = el;
        left = right = null;
    }
}
