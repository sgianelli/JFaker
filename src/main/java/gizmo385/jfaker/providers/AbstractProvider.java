package gizmo385.jfaker.providers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import lombok.Getter;

/**
 * Provides data of the specified type
 * @author Christopher
 *
 */
public abstract class AbstractProvider {
	
	//Final variables
	@Getter private final String providerName;
	private final Random random;
	
	//Instance variables
	@Getter private int numberOfFormats;
	
	//Data generation variables
	
	/**
	 * This will map data generator tags to the data sources that the generated
	 * data will be sourced from. For example, There might be a mapping on 
	 * male and female first names such that:
	 * 		first_name_female -> ["Charlotte", "Jasmine", "Allison"]
	 * 		first_name_male   -> ["Thomas", "Alexander", "George"]
	 * 
	 * Just as likely, there may be a mapping on streets such that:
	 * 		streets -> ["Main", "First", "Second", "Elm"]
	 * 
	 * This will allow dynamic data loading to take place from the XML files
	 * because it means that data will automatically be sorted into their proper 
	 */
	protected Map< String, List<String> > dataGenerators;
	
	/**
	 * This list will contain the valid forms of data generation that can be
	 * provided via this provider. Each of these will have a valid mapping
	 * within {@link #dataGenerators dataGenerators} that will provide data.
	 */
	protected List<String> generationFields;
	
	/**
	 * This list will contain the various formats in which data can be 
	 * generated. For example, a generation formatted as shown below may exist:
	 * 		"{first_name_male} {last_name}"
	 * 
	 * Upon generation, the generator will then generate data based upon the
	 * "first_name_male" field and the "last_name" field and then combine them
	 * according to the defined format to complete data generation.
	 */
	protected List<String> generationFormats;
	
	/**
	 * Creates a generator with the specified name and {@link java.util.Random Random}
	 * instance.
	 */
	public AbstractProvider( String providerName, Random random ) {
		//Assigns final variables
		this.providerName = providerName;
		this.random = random;
		this.numberOfFormats = 0;
		
		//Instantiates generation structures
		this.dataGenerators = new HashMap<>();
		this.generationFields = new ArrayList<>();
		this.generationFormats = new ArrayList<>();
	}
	
	/**
	 * Accesses a random format in the list of formats and returns it
	 * @return A random generation format
	 */
	private final String randomFormat() {
		return this.generationFormats.get( random.nextInt( numberOfFormats ) );
	}
	
	/**
	 * Generates a single string of data
	 * @return A procedurally generated piece of data
	 */
	public final String generateData() {
		//Get a random format
		String formatString = randomFormat();
		
		//Split the format into separate fields
		String[] format = formatString.split( "\\s" );
		
		StringBuilder generatedData = new StringBuilder();
		
		//Generate data based on the sub-formats within the format array
		for( String formatField : format ) {
			List<String> generator = this.dataGenerators.get(formatField);
			generatedData.append( generator.get( random.nextInt(generator.size()) ) );
		}
		
		return generatedData.toString();
	}
	
	/**
	 * Generates a list of data of predetermined length
	 * @param listLength The length of the list
	 * @return A list of length <i>listLength</i> containing generated data
	 */
	public final List<String> generateDataList( int listLength ) {
		//Create output list
		List<String> generatedData = new ArrayList<>();
		
		//Iteratively generate data
		for( int i = 0; i < listLength; i++ )
			generatedData.add( generateData() );
		
		return generatedData;
	}
}
