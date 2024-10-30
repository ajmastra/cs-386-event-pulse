# D5 - Design

In this deliverable, you should describe the architectural design of your system. Structure your deliverable using the following sections. See the  [Team Project Instructions](https://canvas.nau.edu/courses/29116/pages/team-project-%7C-overview "Team Project | Overview")  for details about formatting. Check the lecture materials and perform additional research to produce a high-quality deliverable. As usual, if you have any questions, let me know.

## 1. Description

Provide 1-2 paragraphs to describe your system to help understand the context of your design decisions. You can reuse and update text from the previous deliverables.

_Grading criteria_ (2 points): Completeness; Consistency with the rest of the document; Adequate language.

## 2. Architecture

Present a diagram of the high-level architecture of your system. Use a UML package diagram to describe the main modules and their interrelation. Please check these  [examples](https://www.uml-diagrams.org/package-diagrams-overview.html). Make clear the layers of your architecture (if they exist) as described in  [Multi-Layered Application: UML Model Diagram Example](https://www.uml-diagrams.org/multi-layered-application-uml-model-diagram-example.html).

Provide a brief rationale of your architecture explaining why you designed it that way.

_Grading criteria_ (5 points): Adequate use of UML; Adequate design of an architecture for the system; Adequate description of the rationale.

## 3. Class diagram

Present a refined class diagram of your system, including implementation details such as visibilities, attributes to represent associations, attribute types, return types, parameters, etc. The class diagram should match the code you have produced so far but not be limited to it (e.g., it can contain classes not implemented yet).

The difference between this class diagram and the one you presented in D.3 is that the latter focuses on the domain's conceptual model, while the former reflects the implementation. Therefore, the implementation details are relevant in this case.

_Grading criteria_ (6 points): Adequate use of UML; Adequate choice of classes and relationships; Completeness of the diagram; Adequate presentation of implementation details.

## 4. Sequence diagram

Present a sequence diagram that represents how the objects in your system interact for a specific use case. Also include the use case's description in this section. The sequence diagram should be consistent with the class diagram and architecture.

_Grading criteria_ (5 points): Adequate use of UML; Adequate design of the sequence diagram; Consistency with the class diagram; Consistency with the use case description; Not including the use case description; Over simplistic diagram.

## 5. Design Patterns

Split this section into two subsections. For each subsection, present a UML class diagram showing the application of a design pattern to your system (a different pattern for each section). Each class diagram should contain only the classes involved in the specific pattern (you don’t need to represent the whole system). Choose patterns from two different categories: Behavioral, Structural, and Creational. You are not limited to design patterns studied in class.

Tip: Your system may not be appropriate for any design pattern. In this case, for didactic purposes, be creative and extend the scope of your system slightly to make the design patterns appropriate.

Implement each design pattern in your system and provide GitHub links to the corresponding classes. For example (the links are illustrative, aka fake!):

Car: [https://github.com/user/repo/blob/master/src/com/proj/main/Car.java](https://github.com/user/repo/blob/master/src/com/proj/main/Car.java)

IBreakBehavior: [https://github.com/user/repo/blob/master/src/com/proj/main/IBreakBehavior.java](https://github.com/user/repo/blob/master/src/com/proj/main/IBreakBehavior.java)

BrakeWithABS: [https://github.com/user/repo/blob/master/src/com/proj/main/BrakeWithABS.java](https://github.com/user/repo/blob/master/src/com/proj/main/BrakeWithABS.java)

Brake: [https://github.com/user/repo/blob/master/src/com/proj/main/Brake.java](https://github.com/user/repo/blob/master/src/com/proj/main/Brake.java)

_Grading criteria_ (6 points, 3 for each pattern): Correct use of the design pattern as described in the literature; Adequate choice of the design pattern; Adequate implementation of the design pattern.

## 6. Design Principles

How does your design observe the SOLID principles? Provide a short description of the principles followed and give concrete examples from your classes.

Grading criteria (6 points): Show correct understanding of SOLID principles; Provide enough details to justify how the principles were observed.
