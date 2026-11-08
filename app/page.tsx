import EligibilityFinder, {
  type FinderMapping,
} from "./eligibility-finder";
import eligibilityData from "../magistr_uygunluq.json";

const mappings: FinderMapping[] = eligibilityData.mappings.map((mapping) => ({
  sourcePage: mapping.sourcePage,
  bachelorSpecialties: mapping.bachelorSpecialties,
  programNumber: mapping.programNumber,
  minimumScore: mapping.minimumScore,
  universityMatches: mapping.universityMatches,
}));

export default function Home() {
  return <EligibilityFinder mappings={mappings} />;
}
