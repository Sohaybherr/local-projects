package classes;
import java.util.Set;
import classes.timeslot;


public class section {
    String id;
    String courseCode;
    String instructorId;
    Set<timeslot> schedule;
    Set<String> enrolledStudentIds;
}
