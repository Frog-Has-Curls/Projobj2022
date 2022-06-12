import Fluent
import Vapor

final class Grupaa: Model, Content {
    static let schema = "grupaa"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "grupa")
    var grupa: String
    
	@Field(key: "opis")
    var opis: String
	
	@Field(key: "liczba")
    var liczba: Int
	
	@Parent(key: "orkiestra_id")
    var orkiestra_id: Orkiestra
    
    init() { }

    init(id: UUID? = nil, grupa: String, opis: String, liczba: Int) {
        self.id = id
        self.grupa = grupa
		self.opis = opis
		self.liczba = liczba
    }
}