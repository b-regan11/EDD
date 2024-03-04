package FileSelection;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;


public class FileSelection {
    public static String selectFile() {
        JFileChooser chooser = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                "Excel Files", "xlsx");
        chooser.setFileFilter(filter);
        int returnVal = chooser.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            return chooser.getSelectedFile().getPath();
        } else {
            // Return null or an empty string to indicate no file was selected
            return null;
        }
    }

    public static void main(String[] args) {
        // Example of how to use the selectFile method
        String selectedFileName = selectFile();
        if (selectedFileName != null) {
            System.out.println(selectedFileName);
        }
    }
} 