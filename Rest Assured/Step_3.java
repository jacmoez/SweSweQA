import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.*;

import java.util.HashMap;
import java.util.Map;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class Step_3 {

    private static final String BASE_URL = "https://jsonplaceholder.typicode.com/";

    @BeforeAll
    public static void setUp(){
        RestAssured.baseURI = BASE_URL;
    }

    @Test
    @Order(1)
    public void testCreatePost() {
        Map<String, Object> post = new HashMap<>();
        post.put("title", "New Post");
        given()
                .contentType(ContentType.JSON)
                .body(post)
                .when()
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("id", notNullValue())
                .body("title", equalTo("New Post"));
    }
    @Test
    @Order(2)
    public void testCreatePostWithNumberBody(){
        Map<String, Object> post = new HashMap<>();

        post.put("title", "Number Body Post");
        post.put("body", 29031995);
        post.put("userId", 1);
        given()
                .contentType(ContentType.JSON)
                .body(post)
                .when()
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("body", equalTo(29031995));
        System.out.println("Test 2: Number Body Post Success");
    }

    @Test
    @Order(3)
    public void testCreatePostWithBooleanValues() {
        Map<String, Object> post = new HashMap<>();
        post.put("title", "Boolean Post");
        post.put("isPublished", true);
        post.put("isActive", false);
        post.put("userId", 1);

        given()
                .contentType(ContentType.JSON)
                .body(post)
                .when()
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("isPublished", equalTo(true))
                .body("isActive", equalTo(false))
                        .body("userId", equalTo(1));
        System.out.println("Test 3 : Boolean Post Success");
    }

    @Test
    @Order(4)
    public void testCreateWithNestedObject() {
        Map<String , Object> post = new HashMap<>();
        post.put("title", "Nested Object Post");
        Map<String, Object> details = new HashMap<>();
        details.put("author", "QA Swe Swe");
        details.put("category", "QA Testing");
        post.put("details", details);
        post.put("userId", 1);

        /*
        res body ->
             {
                "title": "Nested Object Post"
                "details": {
                 "author": "QA Swe Swe",
                 "category": "QA Testing"

                },
                "userId": 1,

             }

         */
        given()
                .contentType(ContentType.JSON)
                .body(post)
                .when()
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("details.author", equalTo("QA Swe Swe"))
                .body("details.category", equalTo("QA Testing"));

        System.out.println("Testing 4 : Nest Object Post Success");

    }
}
