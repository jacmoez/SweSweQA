import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.hasSize;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class Step_4 {

    private static final String BASE_URL = "/posts";

    @BeforeEach
    public void setUp(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";
    }

    @ParameterizedTest
    //@CsvFileSource(resources= "create_post_data.csv")
    @CsvFileSource(files = "C:\\Users\\NJ TECH\\IdeaProjects\\swe_swe\\src\\main\\resources\\create_post_data.csv")
//    @CsvSource({
//            "Test Title 1, Test Body 1, 1, 201, Test Title 1",
//            "Test Title 2, Test Body 2, 2, 201, Test Title 2",
//            "Test Title 3, Test Body 3, 1, 201, Test Title 3",
//    })


    public void createPostParameter(String title, String body, String userId, int resStatusCode, String resTitle){
            String requestBody = "{" +
                    (title != null && !title.isEmpty()? "\"title\": \"" + title + "\"," : "" ) +
                    (body != null && !body.isEmpty()? "\"body\": \"" + body + "\"," : "") +
                    (userId != null && !userId.toString().isEmpty()? "\"userId\": \"" + userId + "\"," : "")
                    +"}";

            requestBody = requestBody.replaceAll(",\\s*}$", "}");

        Response response = given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post(BASE_URL)
                .then()
                .extract().response();

        Assertions.assertEquals(resStatusCode, response.getStatusCode());
        if (resTitle != null && resTitle.isEmpty()){
            Assertions.assertEquals(resTitle, response.jsonPath().getString("title"));
        }
        System.out.println("Create Post Parameter Success!");
    }
        @Test
        @Order(1)
        public void testListSize() {
            given()
                    .when()
                    .get("/posts")
                    .then()
                    .assertThat()
                    .body("$", hasSize(100));

            System.out.println("Test 1 : Check Response Total 100");
        }

        public static void main(String[] args) {

        }
    }
