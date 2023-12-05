package sid.org.gatWayService;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.ReactiveDiscoveryClient;
import org.springframework.cloud.gateway.discovery.DiscoveryClientRouteDefinitionLocator;
import org.springframework.cloud.gateway.discovery.DiscoveryLocatorProperties;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class GatWayServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(GatWayServiceApplication.class, args);
	}

	@Bean
	DiscoveryClientRouteDefinitionLocator locator(ReactiveDiscoveryClient rdc, DiscoveryLocatorProperties ldp){
		return  new DiscoveryClientRouteDefinitionLocator(
				rdc,
				ldp
		);
	}

}
